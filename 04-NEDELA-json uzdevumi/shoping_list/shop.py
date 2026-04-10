import sys
import os
import json
from storage import load_list, save_list


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Lietošana: python shop.py [add|list|total|clear] ...")
		sys.exit(1)

	command = sys.argv[1]

	if command == "list":
		items = load_list()
		if not items:
			print("Nav neviena prece iepirkumu sarakstā.")
		else:
			print("Iepirkumu saraksts:")
			for i, item in enumerate(items, 1):
				name = item["name"].capitalize() if isinstance(item, dict) and "name" in item else str(item).capitalize()
				price = item["price"] if isinstance(item, dict) and "price" in item else ""
				quantity = item["quantity"] if isinstance(item, dict) and "quantity" in item else "1"
				print(f"{name} - {price} EUR/gab. x {quantity}")

	elif command == "add":
		if len(sys.argv) < 5:
			print("Lietošana: python shop.py add <name> <price> <quantity>")
			sys.exit(1)
		name = sys.argv[2]
		price = sys.argv[3]
		quantity = sys.argv[4]
		items = load_list()
		items.append({"name": name, "price": price, "quantity": quantity})
		save_list(items)
		print(f"✓ Produkts pievienots: {name} ({price} EUR/gab., daudzums: {quantity})")

	elif command == "total":
		items = load_list()
		if not items:
			print("Nav neviena prece iepirkumu sarakstā.")
		else:
			total = 0
			total_quantity = 0
			for item in items:
				try:
					price = float(item["price"])
					quantity = int(item["quantity"]) if "quantity" in item else 1
					total += price * quantity
					total_quantity += quantity
				except (KeyError, ValueError, TypeError):
					continue
			num_products = len(items)
			print(f"Kopējā summa: {total:.2f} EUR (  vienību skaits: {total_quantity}, produktu skaits: {num_products},)")

	elif command == "clear":
		save_list([])
		print("Iepirkumu saraksts ir izdzēsts.")

	else:
		print(f"Nezināma komanda: {command}")
		print("Lietošana: python shop.py [add|list|total|clear] ...")
		sys.exit(1)
		
