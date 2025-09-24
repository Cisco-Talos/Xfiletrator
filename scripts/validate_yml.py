import os
import yaml
import jsonschema
from pathlib import Path

SCHEMA_PATH = "YML-Schema.yml"
YML_FOLDER = "yml"

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def validate_yml(file_path, schema):
    data = load_yaml(file_path)
    try:
        jsonschema.validate(instance=data, schema=schema)
        print(f"✔ VALID: {file_path}")
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"✖ INVALID: {file_path}\n→ {e.message}\n")
        return False

def main():
    schema = load_yaml(SCHEMA_PATH)
    files = list(Path(YML_FOLDER).glob("*.yml"))
    has_error = False

    for yml_file in files:
        # Skip schema, template, or tag meta files
        if yml_file.name.startswith("YML-") or yml_file.name.startswith("Allowed-"):
            continue
        if not validate_yml(yml_file, schema):
            has_error = True

    if has_error:
        print("One or more YAML files are invalid.")
        exit(1)
    else:
        print("All YAML files are valid.")

if __name__ == "__main__":
    main()
