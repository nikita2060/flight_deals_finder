# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

datamanager = DataManager()
sheet_data = datamanager.sheet_data

def get_city_name():
    for row in sheet_data:
        if row['iataCode'] == '':
            city = row['city']
            FlightSearch.get_iata_code(city)


datamanager.update_sheet()

