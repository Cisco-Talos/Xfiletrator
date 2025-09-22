# Contributing to the Exfiltration Framework

Thank you for your interest in contributing to this project.

This framework documents benign tools that may be abused for data exfiltration, with a focus on features relevant to detection, threat hunting, and forensic analysis.

---

## How to Contribute

You can contribute in several ways:

### 1. Add a New Tool

If you would like to document a new tool:

- Copy an existing YAML file from the `/yml/` folder (e.g., `rclone.yml`)
- Rename it using the lowercase tool name (e.g., `newtool.yml`)
- Fill in all applicable fields using the [field reference](#field-reference)
- Submit a pull request with a clear description of what you’ve added

### 2. Improve an Existing Entry

- Update or complete missing fields
- Add new tags or detection insights
- Fix typos, incorrect values, or outdated references

### 3. Propose New Fields or Tags

- If you think a new feature, category, or tag should be included, open an issue to discuss it
- Please explain why it’s useful and give examples

---

## File Format

All tool entries are stored in the `/yml/` directory. Each file must follow valid [YAML syntax](https://yaml.org/spec/).

Ensure:

- Indentation is consistent (2 spaces)
- All lists are properly formatted with `-` items
- Field names use lowercase and dash-case

---

## Field Reference

| Field            | Description                                                         |
|------------------|---------------------------------------------------------------------|
| `Name`           | Tool name (string)                                                  |
| `Category`       | `native`, `third-party`, or `cloud-based`                           |
| `Platform`       | List of supported platforms (e.g., `Windows`, `Linux`)              |
| `Execution`      | `cli`, `gui`, `api`                                                 |
| `Capabilities`   | List of functional abilities (e.g., `file-transfer`, `cloud-sync`)  |
| `Stealth`        | List of stealth techniques (e.g., `masquerading`, `encrypted-transfer`) |
| `Forensics`      | Dictionary with fields like `BinaryLocations`, `ConfigFiles`, `RegistryKeys`, etc. |
| `ThreatActors`   | Known threat groups using the tool (if applicable)                  |
| `References`     | Links to reports, blogs, or analysis sources                        |
| `Tags`           | Keywords to support filtering (e.g., `ransomware`, `encrypted-transfer`) |

---

## Validation

We may add an automated validation script in the future to:

- Ensure field completeness
- Check YAML syntax
- Enforce tag consistency

Please review your `.yml` file for accuracy before submitting a pull request.

---

## Licensing

By contributing, you agree that your contributions will be licensed under the Apache 2.0 License.

---

## Questions?

Open an issue if you're unsure how to contribute or need help structuring your entry.
