import requests


class FlightSearch:
    def __init__(self):
        self.cities = []

    def get_city_name(self, city):
        self.cities.append(city)

    def respond(self):
        sheet_url = "https://api.sheety.co/0d3b0683421d5adbc5a069b4803ee004/flightDeals/prices"
        response = requests.get(url=sheet_url)
