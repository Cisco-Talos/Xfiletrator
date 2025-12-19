import os
import yaml
import jsonschema
from pathlib import Path

SCHEMA_PATH = "YML-Schema.yml"
YML_FOLDER = "yml"

REQUIRED_TOP_FIELDS = [
    "Name",
    "Description",
    "Category",
    "Platform",
    "Execution",
    "Capabilities",
    "Forensics",
    "NetworkBehavior",
    "ThreatActors",
    "UseCases",
    "Detection",
    "References",
    "LastModified",
]

REQUIRED_FORENSICS_FIELDS = [
    "BinaryLocations",
    "FileNamePatterns",
    "CommandLineArgs",
    "ConfigFiles",
    "RegistryPersistence",
    "LogFiles",
    "NetworkArtifacts",
    "ScheduledTask",
]

REQUIRED_NETWORK_BEHAVIOR_FIELDS = [
    "Description",
    "Behaviors",
]

SKIPPED_PREFIXES = ("YML-", "Allowed-", "README")

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def validate_required_fields(data, file_path):
    missing = [field for field in REQUIRED_TOP_FIELDS if field not in data]
    if missing:
        print(f"✖ MISSING TOP-LEVEL FIELDS in {file_path}:\n→ {missing}\n")
        return False

    forensics = data.get("Forensics", {})
    if not isinstance(forensics, dict):
        print(f"✖ INVALID Forensics type in {file_path} — should be a dictionary\n")
        return False

    missing_forensics = [f for f in REQUIRED_FORENSICS_FIELDS if f not in forensics]
    if missing_forensics:
        print(f"✖ MISSING FORENSICS FIELDS in {file_path}:\n→ {missing_forensics}\n")
        return False

    network_behavior = data.get("NetworkBehavior", {})
    if not isinstance(network_behavior, dict):
        print(f"✖ INVALID NetworkBehavior type in {file_path} — should be a dictionary\n")
        return False

    missing_nb = [f for f in REQUIRED_NETWORK_BEHAVIOR_FIELDS if f not in network_behavior]
    if missing_nb:
        print(f"✖ MISSING NetworkBehavior FIELDS in {file_path}:\n→ {missing_nb}\n")
        return False

    if not isinstance(network_behavior.get("Behaviors"), list):
        print(f"✖ NetworkBehavior.Behaviors must be a list in {file_path}\n")
        return False

    return True

def validate_yml(file_path, schema):
    data = load_yaml(file_path)

    try:
        jsonschema.validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        print(f"✖ INVALID FORMAT: {file_path}\n→ {e.message}\n")
        return False

    return validate_required_fields(data, file_path)

def main():
    if not os.path.exists(YML_FOLDER):
        print(f"ERROR: Folder '{YML_FOLDER}' not found.")
        exit(1)

    schema = load_yaml(SCHEMA_PATH)
    files = list(Path(YML_FOLDER).glob("*.yml"))
    has_error = False

    for yml_file in files:
        if yml_file.name.startswith(SKIPPED_PREFIXES):
            continue
        if not validate_yml(yml_file, schema):
            has_error = True

    if has_error:
        print("❌ One or more YAML files are invalid or incomplete.")
        exit(1)
    else:
        print("✅ All YAML files are valid and complete.")

if __name__ == "__main__":
    main()
