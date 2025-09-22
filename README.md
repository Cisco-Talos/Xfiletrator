# Exfiltration Framework

A structured framework to document and analyze benign tools abused for data exfiltration.  
It highlights detection-relevant features, stealth techniques, and forensic artifacts to support threat hunting, detection engineering, and post-incident analysis.

---

## Purpose

This project provides a centralized knowledge base of legitimate tools that have been observed—or have the potential—to be used for data exfiltration in adversary operations.

While these tools are not inherently malicious, they are often repurposed by threat actors to exfiltrate sensitive information from compromised environments. The goal is to document these tools in a consistent format, making the data easily accessible for defensive use.

---

## Framework Structure

Each tool is documented in its own YAML file, located in the `/yml/` directory. These entries capture:

- Tool metadata (name, category, platform, execution method)
- Capabilities relevant to exfiltration
- Stealth techniques used to avoid detection
- Forensic artifacts left on disk or in memory
- Threat actor usage and external references
- Tags to support filtering and grouping

This format is designed to support both human review and programmatic consumption (e.g., frontends, automation, detection generation).

---

## Repository Layout
```
exfiltration-framework/
├── yml/                      # One YAML file per tool, structured for parsing
│   ├── rclone.yml
│   ├── curl.yml
│   ├── powershell.yml
│   ├── wget.yml
│   ├── pscp.yml
│   ├── azcopy.yml
│   ├── aws-cli.yml
│   ├── dropbox-cli.yml
│   ├── syncthing.yml
│   └── s3browser.yml
│
├── LICENSE                   # Apache License 2.0
├── README.md                 # Project overview and usage
├── CONTRIBUTING.md           # Contribution guidelines
```

---

## Tags

Tools may include tags to help categorize them by behavior, usage, or context. Examples include:

**By Origin:**
- `native`
- `third-party`
- `cloud-based`

**By Execution Type:**
- `cli`
- `gui`
- `api`

**By Detection-Relevant Behavior:**
- `masquerading`
- `encrypted-transfer`
- `scheduled-task`
- `background-execution`

**By Threat Context:**
- `ransomware`
- `apt`
- `initial-access`
- `exfiltration-only`

---

## Contributing

Contributions are welcome.  
If you would like to propose a new tool, improve an existing entry, or suggest new fields or tags, please refer to the contributing guidelines (coming soon).

---

## YAML Validation

To ensure consistency and avoid errors, all tool entries in the `yml/` folder should be validated against the schema defined in `YML-Schema.yml`.

### Install Requirements

Before running the validation script, install the required Python libraries:

```
pip install pyyaml jsonschema
```

### Run the Validator

From the root of the repository, run:

```
python validate_yml.py
```

This will check all .yml files in the yml/ directory (excluding templates and meta files) and print the validation results.

A file is considered invalid if it is missing required fields, contains unsupported tags, or does not conform to the schema.

---

## License

This project is licensed under the Apache License 2.0.  
See the [LICENSE](LICENSE) file for details.

---

## Disclaimer

This framework is intended for educational and defensive purposes only.  
All tools listed are legitimate and not inherently malicious.  
Their inclusion is based on publicly documented misuse by threat actors.
