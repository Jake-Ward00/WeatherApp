$(document).ready(function() {
    $('#weather-form').submit(function(event) {
        event.preventDefault();

        var city = $('#city').val();  // Get the city input from the form

        // Make an AJAX request to the Flask backend
        $.ajax({
            url: '/live_weather',
            type: 'GET',
            data: { city: city },  // Send the city as a query parameter
            success: function(response) {
                if (response.error) {
                    $('#weather-info').html('');
                    $('#error-message').html('<p style="color: red;">' + response.error + '</p>');
                } else {
                    $('#error-message').html('');
                    var weatherHtml = `
                        <h2>Weather in ${response.city}</h2>
                        <p><strong>Temperature:</strong> ${response.temperature}°C</p>
                        <p><strong>Description:</strong> ${response.description}</p>
                        <p><strong>Humidity:</strong> ${response.humidity}%</p>
                        <p><strong>Pressure:</strong> ${response.pressure} hPa</p>
                        <img src="http://openweathermap.org/img/wn/${response.icon}@2x.png" alt="Weather Icon">
                    `;
                    $('#weather-info').html(weatherHtml);
                }
            },
            error: function() {
                $('#weather-info').html('');
                $('#error-message').html('<p style="color: red;">Error fetching data. Please try again.</p>');
            }
        });
    });
});

