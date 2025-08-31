import json
from pathlib import Path

DATA_FILE = Path("data/foods.json")

def load_wrapper(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

class Food():
    def __init__(self, name: str, calories: int, protein: float, fat: float, carbs: float,
                 gluten_free: bool = False, dairy_free: bool = False):
        
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.gluten_free = gluten_free
        self.dairy_free = dairy_free

    def to_dictionary(self):
        return {
            "name": self.name,
            "calories": self.calories,
            "protein": self.protein,
            "fat": self.fat,
            "carbs": self.carbs,
            "gluten_free": self.gluten_free,
            "dairy_free": self.dairy_free,
        }
    
    def __str__(self): 
        return f"{self.name}: {self.calories} cal, {self.protein}g protein, {self.fat}g fat, {self.carbs}g carbs"
    
class FoodManager:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.foods = self.load_foods()

    def load_foods(self): #1.3.3
        try:
            if self.data_file.exists():
                with open(self.data_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    foods = []
                    while data: #1.1.4
                        item = data.pop(0)
                        food = Food(
                            name=item.get("name", ""),
                            calories=item.get("calories", 0),
                            protein=item.get("protein", 0.0),
                            fat=item.get("fat", 0.0),
                            carbs=item.get("carbs", 0.0),
                            gluten_free=item.get("gluten_free", False),
                            dairy_free=item.get("dairy_free", False)
                        )
                        foods.append(food)
                    return foods
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading foods: {e}")
        except Exception as e:
            print(f"Error converting JSON to Food objects: {e}")
        return []

    @load_wrapper #1.2.1
    def add_food(self, name, calories, protein, fat, carbs, gluten_free=False, dairy_free=False):
        food = Food(name, calories, protein, fat, carbs, gluten_free, dairy_free)
        self.foods.append(food)
        self.save_foods()
        return food

    @load_wrapper #1.2.1
    def list_foods(self, sort_by=None):
        foods = self.foods
        if sort_by and sort_by in ["calories", "protein", "fat", "carbs"]:
            foods = sorted(foods, key=lambda x: getattr(x, sort_by)) #1.2.2 & 1.2.3
        return foods

    @load_wrapper
    def get_food(self, name):
        for food in self.foods:
            if food.name == name:
                return food
        return None

    
