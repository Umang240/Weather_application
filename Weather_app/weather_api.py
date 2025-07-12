import requests
from config import API_KEY, BASE_URL
from datetime import datetime

def fetch_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        raise Exception(data.get("message", "Failed to fetch weather"))

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["main"],
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }