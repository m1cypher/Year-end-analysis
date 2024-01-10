# Imports for Obsidian
import frontmatter as pyfront
from yaml.scanner import ScannerError

# Imports for Timular
import requests
import json
from dotenv import load_dotenv
import pandas as pd
from io import StringIO

# Imports for all
import os
from pprint import pprint

script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

if os.path.exists(".env"):
    print(".env file already exist, which means API information should already be there. Skipping questions to gather that information")
else:
    print("The next questions are saved to a .env file that the project ignores.")
    vault = input(r"What is the absolute path for your daily note directory in your Obsidian Vault? ")
    timeular_api_key = input(r"What is your timeular Api Key? This will get saved to the .env file:  ")
    timeular_api_secret = input(r"What is your timeular Api Secret? This will get saved to the .env file:  ")
    with open(".env", "w") as env_file:
        env_file.write(f'TIMEULAR_API_KEY={timeular_api_key}')
        env_file.write(f'TIMEULAR_API_SECRET={timeular_api_secret}')
        env_file.write(f'VAULT_PATH={vault}')





# Frontmatter Documentation https://pypi.org/project/python-frontmatter/
# Primary collection module is pyfront

vault_path = r"C:\Users\emerg\OneDrive\Documents\_Mimir Cyber\Coding\Personal Projects\obsidian-notes\Journal\Daily"

def create_nested_dictionary_from_vault(directory):
    daily_dic = {}

    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)


        if os.path.isfile(file_path):
            # Remove the file extension to get the key
            date_key = os.path.splitext(filename)[0]
            

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    post = pyfront.loads(file.read())
                    daily_dic[date_key] = post.metadata
            except (UnicodeDecodeError, ScannerError) as e:
                print(f"Error in file {filename}: {e}")
                continue  # Skips the file causing the error
                # For complete data, go to the skipped files and fix the errors


    return daily_dic

result_nested_dictionary = create_nested_dictionary_from_vault(vault_path)

pprint(result_nested_dictionary["2023-12-01"]) # Test print of the nested dictionary to make sure it 


ob_df = pd.DataFrame(result_nested_dictionary).T

print(f"I was my heaviest at {ob_df['Weight'].max()} lbs.")
print(f"I was my lightest at {ob_df['Weight'].min()} lbs.")
print(f"That is a loss of {round(ob_df['Weight'].max()) - round(ob_df['Weight'].min())} lbs. for the year")










#### Timeular API Documentation https://developers.timeular.com/#832677a3-73d5-4bde-85dc-40af433414c1 ####

# Secrets will load from ".env"
load_dotenv()
time_api = os.getenv("TIMEULAR_API_KEY")
time_secret = os.getenv("TIMEULAR_API_SECRET")
time_token = os.getenv("TIMEULAR_API_TOKEN")


# Timeular requires you to have an ApiKey and ApiSecret to get your ApiToken. This uses ApiKey and ApiSecret to make the required API Call.
token_payload = json.dumps({
    "apiKey": time_api,
    "apiSecret": time_secret,
})
token_headers = {
    'Content-Type': 'application/json'
}
token_url = "https://api.timeular.com/api/v3/developer/sign-in"
timeular_response_token = requests.request("POST", token_url, headers=token_headers, data=token_payload)
timeular_response_token.raise_for_status()
os.getenv('TIMEULAR_API_TOKEN', timeular_response_token.text)


# With your ApiToken, you can now export data for the dates in question. 
activities_headers = {
  'Authorization': f'Bearer {time_token}'
}
activities_payload = {}
activites_list_url = "https://api.timeular.com/api/v3/report/2023-01-01T00:00:00.000/2023-12-31T23:59:59.999?timezone=America/Chicago"
timeular_response_activites = requests.request("GET", activites_list_url, headers=activities_headers, data=activities_payload)
timeular_response_activites.raise_for_status()


acitivities_text = timeular_response_activites.text

# Setting output to be same directory as jupyter file
script_dir = os.getcwd()
output_file_path = os.path.join(script_dir, 'timeular_data.csv')

# Making the CSV readable for Jupyter manipulation
time_df = pd.read_csv(StringIO(acitivities_text))
time_df = time_df[['Space', 'StartDate', 'Activity', 'Duration', 'Tags']]
time_df.to_csv(output_file_path, index=False)
