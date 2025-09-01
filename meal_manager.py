from food_manager import FoodManager, Food

def load_wrapper(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

class Meals(): #2.1.1
    def __init__(self, name: str, foods: list[Food], type: str):
        self.name = name
        self._foods = foods
        self.__type = type

    def total_nutrients(self):
        total = {
            "calories": 0,
            "protein": 0,
            "fat": 0,
            "carbs": 0
        }
        for food in self._foods:
            total["calories"] += food.calories
            total["protein"] += food.protein
            total["fat"] += food.fat
            total["carbs"] += food.carbs
        return total
    
    def __str__(self):
        nutrients = self.total_nutrients()
        return f"{self.name})- {nutrients["calories"]} cal, {len(self._foods)} items"

    def __repr__(self):
        return f"{self.name}, {self._foods}, {self.__type}, {self.total_nutrients()})"

class Breakfast(Meals): #2.1.3
    def __init__(self, name: str, foods: list[Food]):
        super().__init__(name, foods, "breakfast")

    def __str__(self): #2.1.2
        return f"Breakfast: {self.name}- {self.total_nutrients()["calories"]} cal, {len(self._foods)} items"

class Lunch(Meals):
    def __init__(self, name: str, foods: list[Food]):
        super().__init__(name, foods, "lunch")

    def __str__(self):
        return f"Lunch: {self.name}- {self.total_nutrients()["calories"]} cal, {len(self._foods)} items"

class Dinner(Meals):
    def __init__(self, name: str, foods: list[Food]):
        super().__init__(name, foods, "dinner")

    def __str__(self):
        return f"Dinner: {self.name}- {self.total_nutrients()["calories"]} cal, {len(self._foods)} items"

class MealManager:
    def __init__(self):
        self.meals = []

    def add_meal(self, name, foods: list[Food], type: str):
        if type == "breakfast":
            meal = Breakfast(name, foods)
        elif type == "lunch":
            meal = Lunch(name, foods)
        elif type == "dinner":
            meal = Dinner(name, foods)
        else:
            raise ValueError("Invalid meal type")
        self.meals.append(meal)

    def get_meal(self, name: str) -> Meals | None:
        for meal in self.meals:
            if meal.name == name:
                return meal
        return None

    def list_meals(self) -> list[Meals]:
        return self.meals
    

    
    