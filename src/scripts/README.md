# Helper scripts

`valueset-archive-2-fhir.py` takes all json files of a directory and adds `resourceType: ValueSet` and `url` with given base_url.

```
python valueset-archive-2-fhir.py ../../archive/eu-dcc-valuesets http://example.com
```