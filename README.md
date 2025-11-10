# Xfiletrator: The Exfiltration Mapping Framework

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
│   ├── awscli.yml
│   ├── pscp.yml
│   ├── restic.yml
│   ├── rclone.yml
│   ├── dropboxapi.yml
│   ├── syncthing.yml
│   ├── curl.yml
│   ├── powershell.yml
│   ├── azcopy.yml
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

---

# Setup Guide

This guide provides step-by-step instructions to set up the Exfiltration Framework for local development, validation, and frontend visualization.

---

## Prerequisites

Make sure the following tools are installed on your system.

### 1. Git

Install Git:

```bash
sudo apt install git           # Debian/Ubuntu
brew install git               # macOS with Homebrew
```

### 2. Python 3.8 or higher

Check your version:

```bash
python3 --version
```

Install Python (if needed):

```bash
sudo apt install python3 python3-venv python3-pip      # Debian/Ubuntu
brew install python                                    # macOS with Homebrew
```

### 3. Node.js (v18 or higher) and npm

Check your versions:

```bash
node -v
npm -v
```

Install Node.js and npm:

```bash
sudo apt install nodejs npm                           # Debian/Ubuntu
brew install node                                     # macOS with Homebrew
```

---

## Clone the Repository

```bash
git clone https://github.com/cisco-sbg/exfiltration-framework
cd exfiltration-framework
```

---

## Python Virtual Environment Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate        # Windows

# Install required Python libraries
pip install pyyaml jsonschema
```

---

## Validate YAML Files

After editing or adding `.yml` tool files:

```bash
python scripts/validate_yml.py
```

---

## Generate Frontend Index from YAML Files

```bash
cd scripts
python scripts/generate-index-json.py
cd ..
```

This will generate `exfiltration-ui/public/yml/index.json`.

---

## Frontend Setup

```bash
cd exfiltration-ui
```

### Install Node dependencies

```bash
npm install
```

---

## Run the Frontend Locally

```bash
npm run dev
```

Visit the app in your browser:

```
http://localhost:5173
```

---

## Optional Cleanup

```bash
# Remove frontend build artifacts
cd exfiltration-ui
rm -rf dist

# Deactivate Python virtual environment
deactivate
```

---

## Notes

- Always regenerate `index.json` with `python scripts/generate-index-json.py` after adding new YAML files.
- Tool YAML files go in the `/yml` directory.
- The frontend dynamically loads and visualizes tools listed in `index.json`.

## Allowed Tags and Categories

```yaml
# =========================
# CATEGORIES: General classification of the tool's origin or deployment model
# =========================
categories:
  - native              # Built into the OS (e.g., PowerShell, certutil)
  - third-party         # Tools developed independently from the OS (e.g., rclone, curl)
  - cloud-based         # Tools designed for use with cloud services or platforms (e.g., AWS CLI, Dropbox API)

# =========================
# PLATFORMS: Operating systems supported by the tool
# =========================
platforms:
  - windows             # Microsoft Windows
  - linux               # Linux distributions
  - macos               # Apple macOS

# =========================
# EXECUTION: How the tool is typically executed or interfaced with
# =========================
execution:
  - cli                 # Command-line interface
  - gui                 # Graphical user interface

# =========================
# CAPABILITIES: Functional features relevant to exfiltration
# =========================
capabilities:
  - file-sync              # Continuous synchronization between folders or systems (e.g., rclone, Syncthing).
  - cloud-sync             # Sync or upload to cloud storage platforms like S3, Azure Blob, Dropbox.
  - api-transfer           # Upload via official or custom APIs (e.g., Dropbox API, AWS SDK).
  - direct-to-cloud        # Exfiltrates data directly to cloud endpoints without local staging.
  - selective-upload       # Allows filtering or targeting specific file types or directories.
  - recursive-upload       # Recursively uploads entire folder trees.
  - credentialed-upload    # Requires or supports authenticated uploads (e.g., tokens, IAM keys).
  - anonymous-upload       # Supports unauthenticated uploads (e.g., pre-signed URLs or public buckets).
  - proxy-aware            # Can route traffic through proxies to mask destination.
  - silent-execution       # Executes without user interaction or visible output (used in scripts or automation).
  - portable-execution     # Runs from non-standard paths or without installation (portable binaries).
  - service-identity       # Supports managed identities or service principals (e.g., AzCopy with Azure roles).
  - user-agent-spoofing    # Can spoof or customize the user-agent string in HTTP requests.
  - endpoint-override      # Allows setting custom or attacker-controlled endpoints (e.g., `--endpoint-url`).
  - ftp-upload             # Can exfiltrate via FTP protocol to external servers.
  - header-exfiltration    # Exfiltrates data inside HTTP headers (e.g., `X-Data:`).
  - multipart-upload       # Simulates browser-style form uploads (e.g., using `curl -F`).

# =========================
# FORENSICS: Artifacts and indicators that may appear on a compromised system
# =========================
forensics:
  - binary-location           # Known install or execution paths, especially outside standard directories.
  - config-file-path          # Presence of tool-specific configuration or credential files.
  - command-line-flags        # Flags or arguments used by attackers to trigger upload, sync, or stealth behavior.
  - registry-entry            # Registry keys used to auto-launch or persist the tool (Windows only).
  - scheduled-task-created    # Use of task scheduler or cron to automate tool execution.
  - log-file-location         # Logs written by the tool that may reveal execution or errors.
  - network-indicator         # Domain or API patterns associated with this tool’s upload behavior.

# =========================
# THREAT ACTORS: Types of actors known to abuse the tool
# =========================
threat-actors:
  - apt              # Advanced Persistent Threat groups
  - ransomware       # Ransomware gangs or affiliates


```
