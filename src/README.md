# Usage

Scripts to integrate Valuesets to FHIR server.

`valueset-upload.py` adds all json files on given directory to given FHIR endpoint via http POST.

```
pip install -r requirements.txt
python valueset-importer.py https://github.com/WorldHealthOrganization/tng-valuesets.git knowledgeLibrary http://localhost:8080/fhir/ValueSet
```

Beside command line parameters the input can be provided as environment variables.

## ENV variables

| Environment Variable | Description                                                         | Example Value                                                  |
|----------------------|---------------------------------------------------------------------|----------------------------------------------------------------|
| `REPO_URL`           | The URL of the repository to be cloned.                             | `https://github.com/WorldHealthOrganization/tng-valuesets.git` |
| `DIRECTORY`          | The path to the directory containing the JSON files to be uploaded. | `knowledgeLibrary`                                             |
| `API_ENDPOINT`       | The API endpoint where the JSON files will be uploaded.             | `http://localhost:8080/fhir/ValueSet`                          |


# Docker support

```
docker build -t valueset-importer .
docker run -e REPO_URL=https://github.com/WorldHealthOrganization/tng-valuesets.git -e DIRECTORY=tng-valuesets/knowledgeLibrary -e API_ENDPOINT=https://hapi.fhir.org/baseR4/ValueSet  valueset-importer
```

