# Xfiletrator: The Exfiltration Mapping Framework

A structured framework to document and analyze benign tools abused for data exfiltration.
It highlights detection-relevant features and forensic artifacts to support threat hunting, detection engineering, and post-incident analysis.

---

## Purpose

This project provides a centralized knowledge base of legitimate tools that have been observed—or have the potential—to be used for data exfiltration in adversary operations.

While these tools are not inherently malicious, they are often repurposed by threat actors to exfiltrate sensitive information from compromised environments. The goal is to document these tools in a consistent format, making the data easily accessible for defensive use.

---

## Framework Structure

Each tool is documented in its own YAML file, located in the `/yml/` directory. These entries capture:

- Tool metadata (name, category, platform, execution method)
- Capabilities relevant to exfiltration
- Forensic artifacts left on disk or in memory
- Threat actor usage and external references

This format is designed to support both human review and programmatic consumption (e.g., frontends, automation, detection generation).

---

## Repository Layout

```
exfiltration-framework/
├── yml/                      # One YAML file per tool, structured for parsing
├── LICENSE                   # Apache License 2.0
├── README.md                 # Project overview and usage
├── CONTRIBUTING.md           # Contribution guidelines
```

---

## Field Dictionary

### CATEGORIES

General classification of the tool's origin or deployment model.

- `native` — Built into the OS (e.g., PowerShell, certutil)
- `third-party` — Tools developed independently from the OS (e.g., rclone, curl)
- `cloud-based` — Tools designed for use with cloud services or platforms (e.g., AWS CLI)

### PLATFORMS

Operating systems supported by the tool.

- `windows`
- `linux`
- `macos`

### EXECUTION METHODS

How the tool is typically executed or interfaced with.

- `cli` — Command-line interface
- `gui` — Graphical user interface
- `api` — API-based usage (e.g., REST API, SDK)
- `script` — Indicates that the tool is commonly invoked via external scripts (e.g., PowerShell or Bash), even if it doesn’t have its own scripting language. This flag is retained to distinguish common script-based chaining, although many tools support this.

### CAPABILITIES

Functional capabilities relevant to data exfiltration.

- `file-sync` — Continuous or batched folder synchronization (e.g., Syncthing)
- `cloud-sync` — Interaction with cloud storage platforms
- `api-based-transfer` — File transfers using APIs or SDKs
- `stealth-upload` — Uploads designed to avoid user notification or alerting
- `remote-access` — Includes remote control functionality (e.g., AnyDesk)
- `direct-to-cloud` — Sends data directly to cloud endpoints without storing locally
- `protocol-tunneling` — Can tunnel over other protocols (e.g., SSH over HTTP)

### FORENSIC FIELDS

Expected observable artifacts when the tool is used.

- `BinaryLocations` — Typical paths or known drop locations of the executable
- `CommandLineArgs` — Common arguments that indicate exfiltration behavior
- `ConfigFiles` — Paths to configuration or credential files
- `ScheduledTask` — Tasks that periodically invoke the tool
- `RegistryPersistence` — Registry keys used for startup persistence
- `LogFiles` — Known paths of local logs or outputs
- `NetworkArtifacts` — Observable traffic characteristics (e.g., URLs, domains)

### THREAT ACTORS

Adversaries or threat types known to use the tool.

- `ransomware`
- `apt`

---

## Contributing

Contributions are welcome. If you would like to propose a new tool, improve an existing entry, or suggest new fields, please refer to the `CONTRIBUTING.md`.

---

## YAML Validation

To ensure consistency and avoid errors, all tool entries in the `yml/` folder should be validated against the schema defined in `YML-Schema.yml`.

### Install Requirements

```bash
pip install pyyaml jsonschema
```

### Run the Validator

```bash
python validate_yml.py
```

### Run the Index Generator
```bash
python generate-index-json.py
```

---

## Local Frontend Development

```bash
cd exfiltration-ui
npm install
npm run dev
```

Visit the app in your browser:

```
http://localhost:5173
```

---

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.

---

## Disclaimer

This framework is intended for educational and defensive purposes only. All tools listed are legitimate and not inherently malicious. Their inclusion is based on publicly documented misuse by threat actors.
