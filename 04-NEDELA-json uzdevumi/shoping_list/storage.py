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