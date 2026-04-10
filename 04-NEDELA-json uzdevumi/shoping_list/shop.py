
import sys
import os
import json
from storage import load_list, save_list
from storage import load_prices, save_prices, get_price, set_price
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
			from utils import calc_line_total
			for i, item in enumerate(items, 1):
				name = item["name"].capitalize() if isinstance(item, dict) and "name" in item else str(item).capitalize()
				price = item["price"] if isinstance(item, dict) and "price" in item else ""
				quantity = item["quantity"] if isinstance(item, dict) and "quantity" in item else "1"
				try:
					total_price = calc_line_total(item)
				except Exception:
					total_price = 0
				print(f"{name} - {quantity} x {price} EUR/gab. - {total_price:.2f} EUR")

	elif command == "add":
		if len(sys.argv) < 4:
			print("Lietošana: python shop.py add <nosaukums> <daudzums> [<cena>]")
			sys.exit(1)
		name = sys.argv[2]
		quantity = sys.argv[3]
		if len(sys.argv) >= 5:
			price = sys.argv[4]
			set_price(name, price)
		else:
			price = get_price(name)
			if not price or price == 0.0:
				print(f"Nav atrasta cena produktam '{name}'. Lūdzu, norādiet cenu.")
				sys.exit(1)
		items = load_list()
		item = {"name": name, "quantity": quantity, "price": price}
		items.append(item)
		save_list(items)
		from utils import calc_line_total
		total_price = calc_line_total(item)
		print(f"✓ Produkts pievienots: {name.capitalize()} - {quantity} x {price} EUR/gab. - kopā: {total_price:.2f} EUR")

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
		
