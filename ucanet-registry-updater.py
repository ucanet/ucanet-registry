import os
import shutil
import re
from datetime import datetime


# Constants
REGISTRY_PATH = 'ucanet-registry.txt'

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

BACKUP_PATH = f"ucanet-registry-v1.0-as-at-{now}.txt"

# Regex to match valid IPv4 addresses
IPV4_REGEX = re.compile(r'^\d{1,3}(\.\d{1,3}){3}$', re.IGNORECASE)

def get_registry_version():
    if not os.path.exists(REGISTRY_PATH):
        return "Registry file not found"

    try:
        with open(REGISTRY_PATH, 'r') as file:
            lines = file.readlines()

        has_protoweb_only = True
        has_neocities_or_similar = False
        has_unexpected_word = False

        for line in lines:
            if line.strip().lower() in {
                "20forbeers.com 0 20forbeers.com",
                "erb.pw 0 erb.pw"
            }:
                return "v1.11"


        for line in lines:
            parts = line.strip().split()
            if len(parts) != 3:
                continue  # skip malformed lines

            last = parts[2].lower()

            if IPV4_REGEX.match(last) or last == "protoweb":
                continue

            if any(last.endswith(suffix) for suffix in [".neocities.org", ".free.nf", ".ddns.net"]):
                has_neocities_or_similar = True
                continue

            if '.' not in last:
                if last != "protoweb":
                    has_unexpected_word = True

        # Determine version
        if has_unexpected_word and has_neocities_or_similar:
            return "Corrupted"
        elif has_unexpected_word:
            return "v1.0"
        elif has_neocities_or_similar:
            return "v1.1"
        else:
            return "Unknown"

    except Exception as e:
        return f"Error reading registry: {e}"


def main_menu(version):
    while True:
        print(f"\n=== UCANet Registry {version}  Manager ===")
        if version == "v1.0":
            print("1: Update ucanet registry from v1.0 to v1.1")
        else:
            print("[ ]: ucanet registry already v1.1")

        if version == "v1.1":
            print("2: add osito's useful domain list")
        elif version == "v1.11":
            print("[ ]: osito's useful domain list added")
        else:
            print("[ ]: Update to v1.1 to install osito's useful domain list")

        print("0: Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1" and version == "v1.0":
            version = update_registry()

        elif choice == "2" and version == "v1.1":
            version = ositos_addons()

        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def update_registry():
    print("Starting registry update...")

    if not os.path.exists(REGISTRY_PATH):
        print(f"Error: Registry file not found at '{REGISTRY_PATH}'")
        return

    try:
        # Read the original file
        with open(REGISTRY_PATH, 'r') as file:
            lines = file.readlines()

        updated_lines = []

        for line in lines:
            parts = line.strip().split()
            if len(parts) != 3:
                print(f"Skipping malformed line: {line.strip()}")
                continue

            domain, id_num, address = parts

            if not IPV4_REGEX.match(address) and address.lower() != "protoweb":
                address += ".neocities.org"

            updated_lines.append(f"{domain} {id_num} {address}\n")

        # Backup the original file
        shutil.copyfile(REGISTRY_PATH, BACKUP_PATH)

        # Write the updated content back
        with open(REGISTRY_PATH, 'w') as file:
            file.writelines(updated_lines)

        print("✅ Update successful. Registry saved as:")
        print(f"   Updated: {REGISTRY_PATH}")
        print(f"   Backup : {BACKUP_PATH}")
        return "v1.1"

    except Exception as e:
        print(f"An error occurred during update: {e}")
        return "v1.0"

def ositos_addons(addons_file='addons.txt'):
    # Extract only the domain (first field) from each line in addons.txt
    with open(addons_file, 'r', encoding='utf-8') as f:
        addon_domains = set(line.strip().split()[0].lower() for line in f if line.strip())

    # Read all lines from registry.txt
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        registry_lines = f.readlines()

    updated_registry = []

    for line in registry_lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue

        fields = stripped_line.split()
        if not fields:
            continue

        domain = fields[0].lower()

        if domain in addon_domains:
            print(f"{stripped_line} — this domain will turn over to the collective.")
        else:
            updated_registry.append(line)

    # Overwrite registry.txt with filtered lines
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        f.writelines(updated_registry)

    # Append all lines from addons.txt
    with open(REGISTRY_PATH, 'a', encoding='utf-8') as reg_f, open(addons_file, 'r', encoding='utf-8') as addons_f:
        for line in addons_f:
            if line.strip():
                reg_f.write(line)
    print(f"Useful Domains added.")
    return "v1.11"


if __name__ == "__main__":


    print("* * * * * * * * * * * * * * * * * * * * * * * * *")
    print("* * * Ensure you are either running as root * * *")
    print("* * *or you have ownership over the registry* * *")
    print("* * * * * * * * * * * * * * * * * * * * * * * * *")
    print("🔍 Checking registry version...")
    version = get_registry_version()
    print(f"📄 Detected: Registry {version}")
    main_menu(version)
