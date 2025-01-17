#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

data_man = DataManager()
# pprint(data_manager.get_data())
sheet_data = data_man.get_data()
if sheet_data[0]['iataCode'] == '':
    for city in sheet_data:
        fs = FlightSearch()
        city['iataCode'] = fs.flight_search(city['city'])

pprint(sheet_data)

data_man.add_data(sheet_data)
