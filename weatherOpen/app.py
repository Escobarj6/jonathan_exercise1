from flask import Flask
import requests
import sys
import json

app = Flask(__name__)

@app.route('/temperature/<city>')

def temperature(city):
    payload = {'APPID': '76036279597e9ae0a08f6e58c0ee4144', 'q':city}
    URL = 'http://api.openweathermap.org/data/2.5/weather'
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
