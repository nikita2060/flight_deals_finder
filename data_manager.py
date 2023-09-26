import requests


class DataManager:
    sheet_url = "https://api.sheety.co/0d3b0683421d5adbc5a069b4803ee004/flightDeals/prices"
    response = requests.get(url=sheet_url)
    print(response.text)
