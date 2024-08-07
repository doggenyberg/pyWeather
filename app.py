import os
from flask import Flask, jsonify, render_template, request, send_from_directory
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City parameter not found"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        result = weather_data
    else:
        result = {"error": "Failed to retrieve weather data"}

    return jsonify(result)


@app.route("/images/<path:filename>")
def custom_static(filename):
    return send_from_directory("images", filename)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
