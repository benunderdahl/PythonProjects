import requests
import os
import json
from datetime import datetime

api_key = os.getenv("NUT_X_API_KEY")
id = os.getenv("NUT_X_ID")
nut_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_url = os.getenv("SHEETY")
today = datetime.today().strftime("%d/%m/%Y")
time = datetime.today().strftime('%H:%M:%S')
query = input("What did you do today? ")

payload = {
    "query": query
}
headers = {
        'Content-Type': 'application/json',
        'x-app-id': id,
        'x-app-key': api_key
    }

response = requests.post(url = nut_url, data=json.dumps(payload), headers=headers)
data = response.json()

list_exercises = data["exercises"]
for exercise in list_exercises:
    workouts = {
        "workout": {
        "date": today,
        "time": time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
    }
}

sheety_response = requests.post(url= sheety_url, json=workouts)
print(sheety_response.text)