# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

notification_manager = NotificationManager()
datamanager = DataManager()
sheet_data = datamanager.sheet_data
# print(sheet_data)

def get_city_name():
    for row in sheet_data:
        if row['iataCode'] == '':
            city = row['city']
            code = FlightSearch.get_iata_code(city)
            row['iataCode'] = code


datamanager.update_sheet()
notification_manager.send_sms("do it ashish")

