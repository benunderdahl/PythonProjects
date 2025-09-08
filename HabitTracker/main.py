import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN =
USERNAME =

today = datetime.today()

today = today.strftime("%Y%m%d")
print(today)
params = {
    "date": today,
    "quantity": "1"
}



response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/graph1", json=params, headers = { "X-USER-TOKEN": TOKEN})
print(response.text)