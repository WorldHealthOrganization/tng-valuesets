import os
import subprocess
import sys
import json
import requests

def checkout_repository(repo_url):
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    if not os.path.exists(repo_name):
        # Clone the repository if it does not exist
        subprocess.run(["git", "clone", repo_url], check=True)
    else:
        # Navigate into the directory and pull the latest changes
        os.chdir(repo_name)
        subprocess.run(["git", "pull"], check=True)


#TODO use PUT as upload to support creation and update (Valuesets should use id as filename without .json)
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


# Use the first command line argument as the repository URL, if not provided, use environment variable
repo_url = sys.argv[1] if len(sys.argv) > 1 else os.environ.get('REPO_URL')
checkout_repository(repo_url)

# Use the command line argument as src directory path (knowledge library), if not provided, use environment variable
directory = sys.argv[2] if len(sys.argv) > 2 else os.environ.get('DIRECTORY')

# Use the command line argument as the API endpoint for upload, if not provided, use environment variable
api_endpoint = sys.argv[3] if len(sys.argv) > 3 else os.environ.get('API_ENDPOINT')
upload_valuesets(directory, api_endpoint)