import json
import sys
from jsonschema import validate, ValidationError

def validate_json_schema(json_file, schema_file):
    with open(json_file, 'r', encoding='utf-8') as jf:
        data = json.load(jf)

    with open(schema_file, 'r', encoding='utf-8') as sf:
        schema = json.load(sf)

    try:
        validate(instance=data, schema=schema)
        print("JSON is valid according to the schema.")
    except ValidationError as e:
        print(f"Validation failed: {e.message}")

if __name__ == "__main__":
    json_file = sys.argv[1]
    schema_file = sys.argv[2]
    validate_json_schema(json_file, schema_file)
