import json
import sys
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
	"""Nolasa kontaktus no JSON faila. Ja fails neeksistē, atgriež []."""
	if not os.path.exists(CONTACTS_FILE):
		return []
	with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
		return json.load(f)

def save_contacts(contacts):
	"""Saglabā kontaktu sarakstu JSON failā."""
	with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
		json.dump(contacts, f, indent=2, ensure_ascii=False)

# Command-line interface
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python contacts.py [add|list|search] ...")
		sys.exit(1)

	command = sys.argv[1]

	if command == "list":
		contacts = load_contacts()
		if not contacts:
			print("No contacts found.")
		else:
			for i, contact in enumerate(contacts, 1):
				print(f"{i}. {contact}")

	elif command == "add":
		if len(sys.argv) < 4:
			print("Usage: python contacts.py add <name> <phone>")
			sys.exit(1)
		name = sys.argv[2]
		phone = sys.argv[3]
		contacts = load_contacts()
		contacts.append({"name": name, "phone": phone})
		save_contacts(contacts)
		print(f"Contact added: {name} ({phone})")

	elif command == "search":
		if len(sys.argv) < 3:
			print("Usage: python contacts.py search <name_part>")
			sys.exit(1)
		name_part = sys.argv[2].lower()
		contacts = load_contacts()
		results = [c for c in contacts if name_part in c.get("name", "").lower()]
		if not results:
			print(f"No contacts found matching '{name_part}'.")
		else:
			for i, contact in enumerate(results, 1):
				print(f"{i}. {contact}")

	else:
		print(f"Unknown command: {command}")
		print("Usage: python contacts.py [add|list|search] ...")
