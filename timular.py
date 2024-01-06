import requests
import json
import os
from dotenv import load_dotenv
from pprint import pprint
import pandas as pd
from io import StringIO
import csv

#### Timeular API Documentation https://developers.timeular.com/#832677a3-73d5-4bde-85dc-40af433414c1 ####

load_dotenv()

token_url = "https://api.timeular.com/api/v3/developer/sign-in"

activites_list_url = "https://api.timeular.com/api/v3/report/2023-01-01T00:00:00.000/2023-12-31T23:59:59.999?timezone=America/Chicago"

time_api = os.getenv("TIMEULAR_API_KEY")
time_secret = os.getenv("TIMEULAR_API_SECRET")
time_token = os.getenv("TIMEULAR_API_TOKEN")

token_payload = json.dumps({
    "apiKey": time_api,
    "apiSecret": time_secret,
})

token_headers = {
    'Content-Type': 'application/json'
}


timeular_response_token = requests.request("POST", token_url, headers=token_headers, data=token_payload)
timeular_response_token.raise_for_status()

os.getenv('TIMEULAR_API_TOKEN', timeular_response_token.text)


activities_headers = {
  'Authorization': f'Bearer {time_token}'
}

activities_payload = {}

timeular_response_activites = requests.request("GET", activites_list_url, headers=activities_headers, data=activities_payload)
timeular_response_activites.raise_for_status()

# pprint(timeular_response_activites.text)

acitivities_text = timeular_response_activites.text

# reader = csv.reader(StringIO(acitivities_text))
# headers = next(reader)
# activity_data = next(reader)

script_dir = os.path.dirname(__file__)

output_file_path = os.path.join(script_dir, 'relevant_data.csv')

# with open(output_file_path, 'w', newline='') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(['Workspace', 'Date', 'Duration', 'Activity', 'Tags'])

#     for activity_data in reader:
#         folder, start_date, start_time, end_date, end_time, duration, activity_id, _, activity_type, _, workspace_name, _, user_email, _, tags, _, activity_tags = activity_data
#         relevant_columns = [workspace_name, start_date, duration, activity_type, tags]
#         csv_writer.writerow(relevant_columns)

df = pd.read_csv(StringIO(acitivities_text))
df = df[['workspace_name', 'start_date', 'duration', 'activity_type', 'tags']]
df.to_csv(output_file_path, index=False)