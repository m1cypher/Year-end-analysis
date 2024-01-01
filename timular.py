import requests
import json
import os
from dotenv import load_dotenv

activites_list_url = "https://api.timeular.com/api/v3/report/2023-01-01T00:00:00.000/2023-12-31T23:59:59.999?timezone=America/Chicago"

load_dotenv()


#### Timeular API Documentation https://developers.timeular.com/#832677a3-73d5-4bde-85dc-40af433414c1 ####

time_api = os.getenv("TIMEULAR_API_KEY")
time_secret = os.getenv("TIMEULAR_API_SECRET")

payload = {
    "apikey": time_api,
    "apisecret": time_secret
}

headers = {
    'Content-Type': 'application/json',
    "Authorization": 'Bearer '
}


timeular_response = requests.request("GET", url=activites_list_url, data=payload, headers=headers)
timeular_response.raise_for_status()

time_data = timeular_response.json()

