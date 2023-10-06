# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

notification_manager = NotificationManager()
data_manager = DataManager()
sheet_data = data_manager.sheet_data
flight_search = FlightSearch()


# print(sheet_data)

def get_city_name():
    for row in sheet_data:
        if row['iataCode'] == '':
            city = row['city']
            code = FlightSearch.get_iata_code(city)
            row['iataCode'] = code


data_manager.update_sheet()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# notification_manager.send_sms("do it")
