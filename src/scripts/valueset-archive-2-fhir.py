import os
import json
import sys

def extend_json_files(directory, base_url):
    # Get list of all files in the directory
    files = os.listdir(directory)

    # Filter list for json files
    json_files = [file for file in files if file.endswith('.json')]

    # Create 'out' directory if it doesn't exist
    out_dir = os.path.join(directory, '../../knowledgeLibrary')
    os.makedirs(out_dir, exist_ok=True)

    for json_file in json_files:
        with open(os.path.join(directory, json_file), 'r') as f:
            data = json.load(f)

        # Add new fields
        data['resourceType'] = 'ValueSet'

        # Set 'url' as a concatenation of base URL and filename
        data['url'] = os.path.join(base_url, json_file)

        # Write modified data to new file in 'out' directory
        with open(os.path.join(out_dir, json_file), 'w') as f:
            json.dump(data, f, indent=4)

# Use the first command line argument as the directory path
directory = sys.argv[1]
# Use the second command line argument as the base URL
base_url = sys.argv[2]
extend_json_files(directory, base_url)