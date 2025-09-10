import os
import requests

class FlightSearch:

    def __init__(self):    #This class is responsible for talking to the Flight Search API.
        self._api_key = os.getenv("FLIGHT_API_KEY")
        self._api_secret = os.getenv("FLIGHT_SECRET")
        self._token_url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
        self._get_city = 'https://test.api.amadeus.com/v1/reference-data/locations/'
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=self._token_url, headers=header, data=body)

        return response.json()["access_token"]

    def get_city_info(self, city):
        params = {
            "keyword": city
        }
        response = request.get(self._get_city, params=params, headers)