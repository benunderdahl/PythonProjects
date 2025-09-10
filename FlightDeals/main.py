from flight_search import FlightSearch
from pprint import pprint
import os
import requests


SHEETY_URL = os.getenv("SHEETY")
USERNAME = os.getenv("USER")
PASSWORD = os.getenv("PASS")
flights = FlightSearch()
header = {
    "Authorization": f"bearer {flights._token}"
}

pprint(flights._token)


# data = requests.get(url=SHEETY_URL, auth=(USERNAME, PASSWORD))
# pprint(data.json())