def load_list():
    """Ielādē iepirkumu sarakstu no JSON faila."""
    if not os.path.exists(LIST_FILE):
        return []
    with open(LIST_FILE, "r", encoding="utf-8") as f:
        return json.load(f)