from food_manager import FoodManager, Food

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
    manager = FoodManager()
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
            food = manager.add_food(name, calories, protein, fat, carbs, gluten_free, dairy_free)
            print(f"Added food: {food}")
        elif choice == "2":
            foods = manager.list_foods()
            for f in foods:
                print(f)
        elif choice == "3":
            name = input("Enter food name to search: ")
            food = manager.get_food(name)
            if food:
                print(food)
            else:
                print("Food not found.")
        elif choice == "4":
            sort_by = input("Sort by (calories, protein, fat, carbs): ")
            foods = manager.sort_foods(sort_by)
            for f in foods:
                print(f)
        elif choice == "5":
            filter_type = input("Filter by (gluten-free, dairy-free, both): ")
            foods = manager.list_foods()
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
        #elif choice == "6":
            
        #elif choice == "7":
            
        #elif choice == "8":
           
        elif choice == "9":
            exit = True
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
