import json
import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    url = f"{BASE_URL}?key={API_KEY}&q={CITY}"
    response = requests.get(url).json()
    print(json.dumps(response, indent=2))


if __name__ == "__main__":
    get_weather()
