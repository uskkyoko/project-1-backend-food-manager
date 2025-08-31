from food_manager import FoodManager, Food

def load_wrapper(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

class Meals(): 
    def __init__(self, name: str, foods: list[Food]):
        self.name = name
        self.foods = foods

    def total_nutrients(self):
        total = {
            "calories": 0,
            "protein": 0,
            "fat": 0,
            "carbs": 0
        }
        for food in self.foods:
            total["calories"] += food.calories
            total["protein"] += food.protein
            total["fat"] += food.fat
            total["carbs"] += food.carbs
        return total


class MealManager:
    def __init__(self):
        self.meals = []

    def add_meal(self, meal: Meals):
        self.meals.append(meal)

    def get_meal(self, name: str) -> Meals | None:
        for meal in self.meals:
            if meal.name == name:
                return meal
        return None

    def list_meals(self) -> list[Meals]:
        return self.meals
    
    