import json
from pathlib import Path

DATA_FILE = Path("data/foods.json")

def load_wrapper(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


class Food():
    def __init__(self, name: str, calories: int, protein: float, fat: float, carbs: float,
                 gluten_free: bool, dairy_free: bool):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.gluten_free = gluten_free
        self.dairy_free = dairy_free

    def __str__(self): #2.1.4
        return f"{self.name}: {self.calories} cal, {self.protein}g protein, {self.fat}g fat, {self.carbs}g carbs"
    
    def __repr__(self):
        return f"Food({self.name}, {self.calories}, {self.protein}, {self.fat}, {self.carbs}, {self.gluten_free}, {self.dairy_free})"

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
                    for item in data:
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

    def save_foods(self):
        try:
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            
            data_to_save = [food.__dict__ for food in self.foods]
        
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump(data_to_save, f, ensure_ascii=False, indent=4)
            
            print(f"Successfully saved {len(self.foods)} foods to {self.data_file}")
            
        except (IOError, OSError) as e:
            print(f"Error saving foods (file system): {e}")
        except TypeError as e:
            print(f"Error serializing Food objects to JSON: {e}")
        except Exception as e:
            print(f"Unexpected error saving foods: {e}")


    @load_wrapper #1.2.1
    def add_food(self, name, calories, protein, fat, carbs, gluten_free=False, dairy_free=False):
        food = Food(name, calories, protein, fat, carbs, gluten_free, dairy_free)
        self.foods.append(food)
        self.save_foods()
        return food

    @load_wrapper #1.2.1
    def list_foods(self):
        return self.foods

    @load_wrapper
    def sort_foods(self, sort_by):
        if sort_by and sort_by in ["calories", "protein", "fat", "carbs"]:
            sorted_food = self.foods
            sorted_food = sorted(self.foods, key=lambda x: getattr(x, sort_by))
        return sorted_food

    @load_wrapper
    def get_food(self, name):
        for food in self.foods:
            if food.name == name:
                return food
        return None

    
