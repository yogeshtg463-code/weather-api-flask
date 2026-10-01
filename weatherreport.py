from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "15164c460e64976f41484cdb176efdcc"
BASE_URL = "https://home.openweathermap.org/api_keys"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', default='Mysore')
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        formatted = {
            "city": data.get("name"),
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return jsonify(formatted)
    else:
        print(response.status_code, response.text)
        return jsonify({"error": "Unable to fetch weather data"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
