import datetime

# Function to get weather data
def getWeatherData(weather_resp, flight_time):

    weatherData = {}
    try:
        for time in weather_resp['days'][0]['hours']:

            epoch_time = time['datetimeEpoch']
            dt_obj = datetime.datetime.fromtimestamp(epoch_time)
            military_time_str = dt_obj.strftime('%H%M')
            
            if int(military_time_str) < flight_time:
                weatherData = {
                    'cloudcover': time['cloudcover'],
                    'dew': time['dew'],
                    'humidity': time['humidity'],
                    'precip': time['precip'],
                    'pressure': time['pressure'],
                    'snow': time['snow'],
                    'temp': time['temp'],
                    'visibility': time['visibility'],
                    'windspeed': time['windspeed'],
                    'precipprob': time['precipprob'],
                }
    except:
        print('Error inside getWeatherData function.')
    return weatherData