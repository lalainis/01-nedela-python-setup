
import sys
import os
import json
from storage import load_list, save_list
from utils import calc_line_total
from utils import calc_grand_total, count_units


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
				print(f"{name} -{quantity} x {price} EUR")

	elif command == "add":
		if len(sys.argv) < 5:
			print("Lietošana: python shop.py add <name> <quantity> <price> ")
			sys.exit(1)
		name = sys.argv[2]
		quantity = sys.argv[3]
		price = sys.argv[4]
		items = load_list()
		items.append({"name": name, "quantity": quantity, "price": price})
		save_list(items)
		print(f"✓ Produkts pievienots: {name} (daudzums: {quantity}, {price} EUR)")

	elif command == "total":
		items = load_list()
		if not items:
			print("Nav neviena prece iepirkumu sarakstā.")
		else:
			total = calc_grand_total(items)
			total_quantity = count_units(items)
			num_products = len(items)
			print(f"Kopējā summa: {total:.2f} EUR (vienību skaits: {total_quantity}, produktu skaits: {num_products})")

	elif command == "clear":
		save_list([])
		print("Iepirkumu saraksts ir izdzēsts.")

	else:
		print(f"Nezināma komanda: {command}")
		print("Lietošana: python shop.py [add|list|total|clear] ...")
		sys.exit(1)
		
