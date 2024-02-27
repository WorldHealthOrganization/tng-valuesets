# Usage

Helper script to prepare valuesets for FHIR server.

`valueset-importer.py` takes all json files of a directory and adds `resourceType: ValueSet` and `url` with given base_url.
`valueset-upload.py` adds all json files on given directory to given FHIR endpoint via http POST.

```
pip install requests

python valueset-importer.py ../../archive/eu-dcc-valuesets http://example.com
python valueset-upload.py ../../knowledgeLibrary http://localhost:8080/fhir/ValueSet
```