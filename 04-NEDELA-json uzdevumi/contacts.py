def search_contact(name, filename="contacts.json"):
    """Searches for a contact by name and prints the result."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            contacts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = []
    found = False
    for c in contacts:
        if c['name'].lower() == name.lower():
            print(f"Found: {c['name']} - {c['phone']}")
            found = True
    if not found:
        print(f"No contact found with name '{name}'.")
import json
def list_contacts(filename="contacts.json"):
    """Lists all contacts from the JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            contacts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = []
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for c in contacts:
            print(f"- {c['name']}: {c['phone']}")


# Add a new contact to contacts.json


def add_contact(name, phone, filename="contacts.json"):
    """
    Adds a new contact to the JSON file.
    Args:
        name (str): Contact name.
        phone (str): Contact phone number.
        filename (str): Path to the JSON file.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            contacts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = []
    contacts.append({"name": name, "phone": phone})
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)
    print(f"Contact '{name}' added!")

if __name__ == "__main__":
    while True:
        print("\nContact Manager Menu:")
        print("1. Add new contact")
        print("2. List all contacts")
        print("3. Search contact by name")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            add_contact(name, phone)
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")