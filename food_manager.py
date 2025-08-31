import json
from pathlib import Path

DATA_FILE = Path("data/foods.json")


def load_foods():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_foods(foods):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(foods, f, indent=4)

def add_food(name, calories, protein, fat, carbs):
    foods = load_foods()
    food = {
        "name": name,
        "calories": calories,
        "protein": protein,
        "fat": fat,
        "carbs": carbs
    }
    foods.append(food)
    save_foods(foods)
    return food 

def list_foods(sort_by=None):
    foods = load_foods()
    if sort_by and sort_by in ["name", "calories", "protein", "fat", "carbs"]:
        foods = sorted(foods, key=lambda x: x[sort_by])
    return foods