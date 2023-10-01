import requests
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")


class FlightSearch:
    # def __init__(self):
    #     self.cities = []

    # def respond(self):
    #     sheet_url = "https://api.sheety.co/0d3b0683421d5adbc5a069b4803ee004/flightDeals/prices"
    #     response = requests.get(url=sheet_url)

    def get_iata_code(city):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        header = {"api_key": TEQUILA_API_KEY}
        param = {"term": city, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=header, params=param)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
