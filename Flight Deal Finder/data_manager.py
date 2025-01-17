import requests
from datetime import *
from pprint import pprint


class DataManager:
    def __init__(self):
        self.spreadsheet = "https://api.sheety.co/402ba88f3d39f1b6cae992763ad0200e/flightDealsProject/prices"

        self.header = {
            "Authorization": "Basic bnVsbDpudWxs"
        }

        self.data = requests.get(url=self.spreadsheet, headers=self.header).json()

    def get_data(self):
        return self.data['prices']

    def add_data(self, data):
        for row in data:
            params = {
                "price": {
                    "iataCode": row['iataCode'],
                }
            }
            response = requests.put(url=self.spreadsheet+f"/{row['id']}", json=params, headers=self.header)
            pprint(response)


