# ucanet Registry Updater

This Python script provides a simple command-line interface to manage and update the `ucanet-registry.txt` file used by the ucanet system. The script is modular, making it easy to extend with additional features in the future.

---

## 📦 Features

- Menu-driven interface for managing registry updates
- Backup of original registry file before any changes are made
- Validates and updates registry entries based on specific formatting rules
- Clear terminal output for user feedback

---

## 🔧 Current Functionality

### Option 1: Update ucanet Registry from Version 1.0 to 1.1

Reads the file:
ucanet-registry.txt

Each line in this file is expected to have the following structure:

[ucanet domain name] [ucanet owner id] [internet IP address/or behavior identfying name]

**Update Rules**:
- If the third field (`<address>`) is a valid IP address (e.g. `192.168.1.1`) or the word `protoweb`, it remains unchanged.
- If the third field is anything else (e.g. `downloadfilesfree33`), it will have `.neocities.org` appended to it (e.g. `downloadfilesfree33.neocities.org`).

**Files Written**:
- A backup of the original file is saved as:  
  `../ucanet-registry/ucanet-registry-v1.0.txt`
- The updated file is saved as:  
  `../ucanet-registry/ucanet-registry.txt`

### Option 0: Exit  
Closes the application.

---

## 🚀 How to Run

### Requirements
- Python 3.6+

### Run the Script
python ucanet-registry-updater.py
