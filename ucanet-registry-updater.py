import os
import shutil
import re

# Constants
REGISTRY_PATH = 'ucanet-registry.txt'
BACKUP_PATH = 'ucanet-registry-v1.0.txt'

# Regex to match valid IPv4 addresses
IPV4_REGEX = re.compile(r'^\d{1,3}(\.\d{1,3}){3}$', re.IGNORECASE)

def main_menu():
    while True:
        print("\n=== UCANet Registry Manager ===")
        print("1: Update ucanet registry from version 1.0 to version 1.1")
        print("0: Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            update_registry()
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

    except Exception as e:
        print(f"An error occurred during update: {e}")

if __name__ == "__main__":
    main_menu()
