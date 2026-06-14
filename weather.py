import requests

from config import API_KEY, LAT, LON


def get_weather():

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?lat={LAT}"
        f"&lon={LON}"
        f"&appid={API_KEY}"
        "&lang=ja"
    )

    response = requests.get(url)

    data = response.json()

    return data

def is_thunderstorm(data):

    weather = data["weather"][0]["main"]

    return weather == "Thunderstorm"