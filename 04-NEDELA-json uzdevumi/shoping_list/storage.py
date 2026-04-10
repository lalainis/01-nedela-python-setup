import json
import sys
import os

LIST_FILE = "shopping.json"

PRICES_FILE = "prices.json"

def load_list():
    """Ielādē iepirkumu sarakstu no JSON faila."""
    if not os.path.exists(LIST_FILE):
        return []
    with open(LIST_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_list(items):
    """Saglabā iepirkumu sarakstu JSON failā."""
    with open(LIST_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

def load_prices():      
    """Ielādē cenu sarakstu no JSON faila."""
    if not os.path.exists(PRICES_FILE):
        return {}
    with open(PRICES_FILE, "r", encoding="utf-8") as f:
        return json.load(f) 
        
def save_prices(prices):
    """Saglabā cenu sarakstu JSON failā."""
    with open(PRICES_FILE, "w", encoding="utf-8") as f:
        json.dump(prices, f, ensure_ascii=False, indent=2) 

def get_price(item_name):
    """Iegūst preces cenu no cenas saraksta."""
    prices = load_prices()
    val = prices.get(item_name, 0.0)
    if isinstance(val, dict):
        return val.get('active', 0.0)
    return val

def set_price(item_name, price):
    """Iestata preces cenu cenas sarakstā."""
    import datetime
    prices = load_prices()
    now = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
    prev = prices.get(item_name)
    if isinstance(prev, dict):
        prev_price = prev.get('active')
    else:
        prev_price = prev
    if prev_price and str(prev_price) != str(price):
        inactive = prices.get(item_name + '_inactive', [])
        inactive.append({"price": prev_price, "timestamp": now})
        prices[item_name + '_inactive'] = inactive
    prices[item_name] = {"active": price}
    save_prices(prices)
