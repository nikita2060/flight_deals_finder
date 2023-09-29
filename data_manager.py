import requests
import json
SHEETY_ENDPOINT = "https://api.sheety.co/0d3b0683421d5adbc5a069b4803ee004/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.sheet_data = []
        self.get_sheet_data()

    def get_sheet_data(self):

        response = requests.get(url=SHEETY_ENDPOINT)
        flight_data_dict = json.loads(response.text)  # using json.loads() to convert json formatted string into  dictionary

        self.sheet_data = flight_data_dict["prices"]
    def update_sheet(self):
        for item in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": item["iataCode"]

                        }
            }

            sheet_url = f"{SHEETY_ENDPOINT}/{item['id']}"
            response = requests.put(url=sheet_url, json=new_data)
            print(response.text)

