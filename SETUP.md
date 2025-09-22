# Exfiltration Framework – Setup Guide

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
python validate_yml.py
```

---

## Generate Frontend Index from YAML Files

```bash
cd scripts
python generate-index-json.py
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

## Project Structure Overview

```
exfiltration-framework/
│
├── yml/                      # YAML metadata files
├── validate_yml.py          # YAML schema validator
├── scripts/
│   └── generate-index-json.py   # Auto-generates UI index from YAML files
│
└── exfiltration-ui/         # Frontend UI (React + Tailwind)
    ├── public/yml/index.json    # Auto-generated index
    ├── src/                     # Frontend components
    ├── tailwind.config.js
    ├── vite.config.js
    └── package.json
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
