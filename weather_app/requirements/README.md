# Weather App

A weather app that allows users to get real time weather info for any city, compare real time weather info between multiple cities using a bar chart and a global warming analysis based on historical temperature data using NASAs data

## Setup Instructions

1. Make the repository:
    
    cd 'C:\\Users\\jakew\\OneDrive - Technological University Dublin\\weather_app\\app.py

2. Install dependencies:
    
    pip install -Flask requests pandas numpy matplotlib scikit-learn

    

3. Get an API Key from [OpenWeatherMap](https://openweathermap.org/api) and add it to `app.py`.

4. Run the app:
    
    python3 app.py
   

5. Visit `http://127.0.0.1:5000/` to access the app

## Features
- Home Page: The main page with links to different features of the app.
- Live Weather: Enter the name of a city to fetch the current weather data, including temperature, humidity, and pressure
- City Comparison: Enter multiple cities separated by commas to compare their temperatures on a bar chart
- Global Warming Analysis: View historical global temperature data and forecast future temperature anomalies due to climate change using NASAs data

## Functionalities of the functions
1. Live Weather:
- Description: Allows the user to input a city name to get real time weather info
- Functionality: Uses the OpenWeatherMap API to fetch current weather data and display temperature, humidity, pressure, and weather description
2. City Comparison
- Description: Allows the user to input multiple cities and compare their temperatures in a bar chart
- Functionality: The user can enter a comma separated list of cities and the app fetches the current temperature for each city, it then generates a bar chart comparing these temperatures
3. Global Warming Analysis
- Description: Displays historical global temperature anomalies and predicts future temperature changes due to climate change
- Functionality: The application loads a CSV file containing historical temperature data from NASA, processes it using Pandas, and then uses linear regression to predict future temperature anomalies, it also generates a graph showing both historical and predicted temperature data.
 

## Technologies Used
Backend:

- Python (Flask)
- pandas (for data manipulation)
- numpy (for numerical computations)
- matplotlib (for creating plots)
- scikit-learn (for machine learning predictions)

Frontend:

- HTML - for the structure of the web pages
- CSS - for styling the web pages
- JavaScript - for adding interactivity and dynamic content, particularly AJAX for city comparison
- External APIs - OpenWeatherMap API (for real-time weather data)

## List of Python and Javascript packages
Python:
- Flask - Web framework for creating the web application
- requests - For making HTTP requests to external APIs
- pandas - For handling and manipulating data (reading the CSV and cleaning the data).
- numpy - For handling numerical data and operations
- matplotlib - For creating plots and visualising data
- scikit-learn - For implementing linear regression and predictions

JavaScript:
- AJAX - For dynamically fetching data from the backend and updating the webpage without reloading
- jQuery - Used to handle asynchronous requests and DOM manipulation
