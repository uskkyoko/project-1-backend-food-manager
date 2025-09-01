from food_manager import FoodManager, Food
from meal_manager import MealManager, Breakfast, Lunch, Dinner

def menu_foods():
    print("1. Add food")
    print("2. List foods")
    print("3. Get food")
    print("4. Sort foods")
    print("5. Filter foods")
    print("6. Add a meal")
    print("7. List my meals")
    print("8. Get a meal")
    print("9. Exit")
    choice = input("Choose an option: ")
    return choice

def main():
    food_manager = FoodManager()
    meal_manager = MealManager()
    exit = False
    while not exit:
        choice = menu_foods()

        if choice == "1":
            name = input("Enter food name: ")
            calories = int(input("Enter calories: "))
            protein = float(input("Enter protein: "))
            fat = float(input("Enter fat: "))
            carbs = float(input("Enter carbs: "))
            gluten_free = bool(input("Is it gluten-free? (True/False): "))
            dairy_free = bool(input("Is it dairy-free? (True/False): "))
            food = food_manager.add_food(name, calories, protein, fat, carbs, gluten_free, dairy_free)
            print(f"Added food: {food}")

        elif choice == "2":
            foods = food_manager.list_foods()
            for f in foods:
                print(f)

        elif choice == "3":
            name = input("Enter food name to search: ")
            food = food_manager.get_food(name)
            if food:
                print(food)
            else:
                print("Food not found.")

        elif choice == "4":
            sort_by = input("Sort by (calories, protein, fat, carbs): ")
            foods = food_manager.sort_foods(sort_by)
            for f in foods:
                print(f)

        elif choice == "5":
            filter_type = input("Filter by (gluten-free, dairy-free, both): ")
            foods = food_manager.list_foods()
            if filter_type == "gluten-free":
                foods = [ f for f in foods if f.gluten_free ]
            elif filter_type == "dairy-free":
                foods = [ f for f in foods if f.dairy_free ]
            elif filter_type == "both":
                foods = [ f for f in foods if f.gluten_free and f.dairy_free ]
            else:
                print("No foods matching your criteria.")
            for f in foods:
                print(f)

        elif choice == "6":
            name = input("Enter meal name: ")
            type = input("Enter meal type (breakfast, lunch, dinner): ")
            foods = []
            exit_food = False
            while not exit_food:
                food_name = input("Enter food name to add to meal (or 'done' to finish): ")
                if food_name.lower() == 'done':
                    exit_food = True
                    break
                food = food_manager.get_food(food_name)
                if food:
                    foods.append(food)
                    print(f"Added {food.name} to meal.")
                else:
                    print("Food not found.")
            if foods:
                meal = meal_manager.add_meal(name, foods, type)
            else:
                print("No foods added to meal.")

        elif choice == "7":
            meals = meal_manager.list_meals()
            for m in meals:
                print(m)

        elif choice == "8":
            name = input("Enter meal name to search: ")
            meal = meal_manager.get_meal(name)
            if meal:
                print(meal)
            else:
                print("Meal not found.")

        elif choice == "9":
            exit = True
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
