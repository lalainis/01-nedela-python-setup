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

# komandu apstrāde
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Lietošana: python contacts.py [add|list|search] ...")
		sys.exit(1)

	command = sys.argv[1]

	if command == "list":
		contacts = load_contacts()
		if not contacts:
			print("Nav šādu kontaktu.")
		else:
			print("Kontakti:")
			for i, contact in enumerate(contacts, 1):
				name = contact["name"] if isinstance(contact, dict) and "name" in contact else str(contact)
				phone = contact["phone"] if isinstance(contact, dict) and "phone" in contact else ""
				print(f"{i}. {name} {phone}")

	elif command == "add":
		if len(sys.argv) < 4:
			print("Lietošana: python contacts.py add <name> <phone>")
			sys.exit(1)
		name = sys.argv[2]
		phone = sys.argv[3]
		contacts = load_contacts()
		contacts.append({"name": name, "phone": phone})
		save_contacts(contacts)
		print(f"✓ Kontakts pievienots: {name} ({phone})")

	elif command == "search":
		if len(sys.argv) < 3:
			print("Lietošana: python contacts.py search <name_part>")
			sys.exit(1)
		name_part = sys.argv[2].lower()
		contacts = load_contacts()
		results = [c for c in contacts if name_part in c.get("name", "").lower()]
		if not results:
			print(f"Nav kontaktu, kas atbilst '{name_part}'.")
		else:
			print(f"Atrasti ({len(results)}) kontakti:")
			for i, contact in enumerate(results, 1):
				name = contact["name"] if isinstance(contact, dict) and "name" in contact else str(contact)
				phone = contact["phone"] if isinstance(contact, dict) and "phone" in contact else ""
				print(f"{i}. {name} {phone}")

	else:
		print(f"Nezināma komanda: {command}")
		print("Lietošana: python contacts.py [add|list|search] ...")
