from flask import Flask
import requests
import time
import sys
import json

app = Flask(__name__)

@app.route('/temperature/<city>')
def temperature(city):
    payload = {'APPID': '76036279597e9ae0a08f6e58c0ee4144', 'q':city}
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    weather = requests.get(URL, params=payload)
    response = requests.get(URL, params=payload)
    if response.status_code == 200:
        print('Success!', file = sys.stdout)
    elif response.status_code == 404:
        print('Error! Not Found', file = sys.stdout)

    response_json = response.json()
    formatted_response = json.dumps(response_json, indent=2)
    print(formatted_response, file = sys.stdout)

    temperature = response_json['main']['temp']
    s = '<h> Current temperature in {} is {:0.2f} Celsius. </s>'
    return s.format(city, temperature - 273)

""" whatCity = input("What city would you like to view the temperature from?")
weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+whatCity+'&appid=76036279597e9ae0a08f6e58c0ee4144')
url = ('http://api.openweathermap/data/2.5/weather?q='+whatCity+'&appid=76036279597e9ae0a08f6e58c0ee4144')

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

data = weather.json()

temp = data['main']['temp']
description = data['main']['weather'][0]['description']
printWeather = "In {}, the weather is currently {} degrees Celsius with {}."
spinMeRightRound = spinning_cursor()
for _ in range(25):
    sys.stdout.write(next(spinMeRightRound))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')

convert = int(temp - 273.15)
print(printWeather.format(weather, convert, description)) """