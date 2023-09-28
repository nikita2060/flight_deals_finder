import requests
import json


class DataManager:
    def __init__(self):
        self.sheet_data = []
        self.get_sheet_data()

    def get_sheet_data(self):
        sheet_url = "https://api.sheety.co/0d3b0683421d5adbc5a069b4803ee004/flightDeals/prices"
        response = requests.get(url=sheet_url)
        flight_data_dict = json.loads(response.text)  # using json.loads() to convert json formatted string into  dictionary

        self.sheet_data = flight_data_dict["prices"]

    def update_sheet(self):
        sheet_url = "https://api.sheety.co/0d3b0683421d5adbc5a069b4803ee004/flightDeals/prices/1"
        response = requests.put(url=sheet_url)
        print(response.text)

