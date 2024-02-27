import os
import json
import requests
import sys

def upload_valuesets(directory, api_endpoint):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            # Open the JSON file and load its content
            with open(os.path.join(directory, filename), 'r') as f:
                data = json.load(f)

            # Make a POST request to the API endpoint with the JSON content
            headers = {
                'accept': 'application/fhir+json',
                'Content-Type': 'application/fhir+json'
            }
            response = requests.post(api_endpoint, headers=headers, json=data)

            # Check if the request was successful
            if response.status_code != 201:
                print(f'Error: Failed to upload {filename}. Status code: {response.status_code}')
            else:
                print(f'Successfully uploaded {filename}')

# Use the first command line argument as the directory path
directory = sys.argv[1]
# Use the second command line argument as the API endpoint
api_endpoint = sys.argv[2]
upload_valuesets(directory, api_endpoint)