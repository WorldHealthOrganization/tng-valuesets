import os
import subprocess
import sys
import json
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def checkout_repository(repo_url):
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    if not os.path.exists(repo_name):
        # Clone the repository if it does not exist
        subprocess.run(["git", "clone", repo_url], check=True)
    else:
        # Navigate into the directory and pull the latest changes
        os.chdir(repo_name)
        subprocess.run(["git", "pull"], check=True)


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

            # Remove .json from filename and add it to the api_endpoint and as id of payload
            filename_without_extension, _ = os.path.splitext(filename)
            data['id'] = filename_without_extension
            api_endpoint_id = f"{api_endpoint}/{filename_without_extension}"

            print(f'PUT {api_endpoint_id}')
            response = requests.put(api_endpoint_id, headers=headers, json=data)

            # Check if the request was successful
            if response.status_code == 200:
                logging.info(f'Successfully updated {filename}')
            elif response.status_code == 201:
                logging.info(f'Successfully created {filename}')
            else:
                logging.error(f'Failed to upload {filename}. Status code: {response.status_code}, Response body: {response.text}')


# Use the first command line argument as the repository URL, if not provided, use environment variable
repo_url = sys.argv[1] if len(sys.argv) > 1 else os.environ.get('REPO_URL')
checkout_repository(repo_url)

# Use the command line argument as src directory path (knowledge library), if not provided, use environment variable
directory = sys.argv[2] if len(sys.argv) > 2 else os.environ.get('DIRECTORY')

# Use the command line argument as the API endpoint for upload, if not provided, use environment variable
api_endpoint = sys.argv[3] if len(sys.argv) > 3 else os.environ.get('API_ENDPOINT')
upload_valuesets(directory, api_endpoint)