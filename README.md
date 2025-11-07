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
  - api                 # API-based usage (e.g., REST API, SDK)
  - script              # Invoked via script (e.g., batch, bash, ps1)

# =========================
# CAPABILITIES: Functional capabilities relevant to exfiltration
# =========================
capabilities:
  - file-sync              # Continuous folder synchronization (e.g., Syncthing, rclone in sync mode)
  - cloud-sync             # Sync with cloud storage platforms
  - api-based-transfer     # File transfers initiated via API
  - stealth-upload         # Designed or abused to quietly upload without alerting the user
  - remote-access          # Provides full remote access capabilities
  - direct-to-cloud        # Uploads directly to cloud endpoints without local storage
  - protocol-tunneling     # Can be used to tunnel traffic over other protocols (e.g., HTTP, DNS)

# =========================
# STEALTH: Tactics/tools may use to hide behavior or avoid detection
# =========================
stealth:
  - masquerading              # Disguising the tool as a legitimate file or process
  - encrypted-transfer        # Use of encrypted channels (e.g., TLS) to avoid inspection
  - api-based-transfer        # Using cloud APIs to mimic legitimate user activity
  - background-execution      # Running silently in the background or without user interaction
  - proxy-support             # Can use proxies to hide real IP/destination
  - port-obfuscation          # Uses non-standard ports or port-hopping
  - user-agent-manipulation   # Spoofs or manipulates user-agent headers
  - scriptable                # Easily embedded in larger scripts or malicious chains

# =========================
# FORENSICS: Artifacts and indicators that may appear on a compromised system
# =========================
forensics:
  - custom-config-location    # Uses or allows non-default config file paths
  - scheduled-task            # Can be triggered via Windows Task Scheduler or cron
  - registry-persistence      # Persists in Windows Registry (e.g., Run keys)
  - auto-start-entry          # Creates entries to auto-launch at startup
  - logs-artifacts            # Leaves logs or known traces
  - known-binary-location     # Binary typically resides in a known location
  - suspicious-command-line   # Invoked with arguments commonly seen in attacks
  - tls-connection            # Initiates encrypted connections over TLS

# =========================
# THREAT ACTORS: Types of actors known to abuse the tool
# =========================
threat-actors:
  - apt              # Advanced Persistent Threat groups
  - ransomware       # Ransomware gangs or affiliates
  - redteam          # Used in red teaming / adversary simulation
  - pentest-tool     # Known or intended for penetration testing
  - commodity        # Widely used, freely available malware or toolset

# =========================
# TAGS: Freeform labels for UI filtering or detection enrichment
# =========================
tags:
  - stealth                  # Generic stealth indicator
  - commonly-used            # Frequently found in real-world incidents
  - lolbas                   # Appears in LOLBAS or similar reference lists
  - cloud-tool               # Associated with cloud service interaction
  - remote-execution         # Enables control or execution from a remote host
  - persistence              # Capable of maintaining persistence on the system

```