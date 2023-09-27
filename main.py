# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager

datamanager = DataManager()
sheet_data = datamanager.sheet_data
city = []


def get_city_name():
    for row in sheet_data:
        if row['iataCode'] == '':
            city.append(row['city'])

get_city_name()
print(city)

