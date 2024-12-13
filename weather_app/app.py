import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from sklearn.linear_model import LinearRegression
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# OpenWeatherMap API key
API_KEY = '41a8c74a38ee11e2503f3527f0a59afc'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def index():
    # render homepage with links to live weather and city comparison
    return render_template('index.html')

@app.route('/live_weather', methods=['GET', 'POST'])
def live_weather():
    if request.method == 'POST':
        # get the city entered by the user
        city = request.form['city']
        
        if not city:
            return render_template('live_weather.html', error="No city provided.")
        
        # construct the full API URL
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data.get("cod") != 200:
                return render_template('live_weather.html', error="City not found or invalid API request.")

            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
            }

            return render_template('live_weather.html', weather=weather)
        else:
            return render_template('live_weather.html', error="City not found or invalid API request.")
    
    return render_template('live_weather.html')

@app.route('/comparison', methods=['GET', 'POST'])
def comparison():
    if request.method == 'POST':
        cities_input = request.form['cities']
        cities = [city.strip() for city in cities_input.split(',')]

        weather_data = []

        for city in cities:
            url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                weather_data.append({
                    "city": data["name"],
                    "temperature": data["main"]["temp"]
                })

        fig, ax = plt.subplots()
        city_names = [data['city'] for data in weather_data]
        temperatures = [data['temperature'] for data in weather_data]

        ax.bar(city_names, temperatures)
        ax.set_xlabel('Cities')
        ax.set_ylabel('Temperature (°C)')
        ax.set_title('City Temperature Comparison')

        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        img_data = base64.b64encode(img.read()).decode('utf-8')

        return render_template('comparison.html', img_data=img_data, cities=cities)

    return render_template('comparison.html', img_data=None)

# route for global warming analysis
@app.route('/global_warming', methods=['GET'])
def global_warming():
    # load the CSV data with proper headers
    df = pd.read_csv('static/global_temperature_data.csv', header=1)

    # clean the 'J-D' column by converting non-numeric values to NaN
    df['J-D'] = pd.to_numeric(df['J-D'], errors='coerce')

    # drop rows where 'J-D' has NaN values
    df = df.dropna(subset=['J-D'])

    # now access the 'Year' and 'J-D' columns
    df = df[['Year', 'J-D']]

    # linear regression to predict future temperatures
    X = df['Year'].values.reshape(-1, 1)  # independent variable (Year)
    y = df['J-D'].values  # dependent variable (Temperature Anomaly)

    model = LinearRegression()
    model.fit(X, y)

    # predict future temperatures
    future_years = np.array([2025, 2030, 2040, 2050]).reshape(-1, 1)
    future_temperatures = model.predict(future_years)

    # create a DataFrame for future predictions
    future_data = pd.DataFrame({
        'Year': future_years.flatten(),
        'Predicted Temperature': future_temperatures
    })

    # plot historical temperature anomaly and future predictions
    fig, ax = plt.subplots()
    ax.plot(df['Year'], df['J-D'], label='Historical Data', color='blue', marker='o')
    ax.plot(future_data['Year'], future_data['Predicted Temperature'], label='Forecasted Temperature', color='red', linestyle='--')
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature Anomaly (°C)')
    ax.set_title('Global Temperature Anomaly Due to Global Warming')
    ax.legend()

    # save plot to image (base64 encoding for embedding in HTML)
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_data = base64.b64encode(img.read()).decode('utf-8')

    return render_template('global_warming.html', img_data=img_data, future_data=future_data.to_html(classes='dataframe', header=True))


if __name__ == '__main__':
    app.run(debug=True)
