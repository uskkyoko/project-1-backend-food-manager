import argparse
from food_manager import FoodManager 


def main():
    manager = FoodManager()
    parser = argparse.ArgumentParser(
        prog="diet_planner",
        description="A simple Diet Planner. Manage foods, track nutrients, and filter based on diet preferences."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    add_parser = subparsers.add_parser("add-food", help="Add a new food to the database")
    add_parser.add_argument("--name", required=True, help="Name of the food")
    add_parser.add_argument("--calories", type=int, required=True, help="Calories in the food item")
    add_parser.add_argument("--protein", type=float, required=True, help="Protein content in grams")
    add_parser.add_argument("--fat", type=float, required=True, help="Fat content in grams")
    add_parser.add_argument("--carbs", type=float, required=True, help="Carbohydrate content in grams")
    add_parser.add_argument("--gluten-free", action="store_true", help="Is the food gluten-free?")
    add_parser.add_argument("--dairy-free", action="store_true", help="Is the food dairy-free?")

    list_parser = subparsers.add_parser("list-foods", help="List foods from the the database")
    list_parser.add_argument("--sort", choices=["calories", "protein", "fat", "carbs"], help="Sort foods by a specific nutrient")

    get_parser = subparsers.add_parser("get-food", help="Get details of a specific food")
    get_parser.add_argument("--name", required=True, help="Name of the food to retrieve")

    filter_parser = subparsers.add_parser("filter-foods", help="Filter foods based on dietary preferences")
    filter_parser.add_argument("--gluten-free", action="store_true", help="Filter for gluten-free foods")
    filter_parser.add_argument("--dairy-free", action="store_true", help="Filter for dairy-free foods")

    args = parser.parse_args()

    if args.command == "add-food":
        food = manager.add_food(args.name, args.calories, args.protein, args.fat, args.carbs, args.gluten_free, args.dairy_free)
        print(f"Added food: {food}")
    elif args.command == "list-foods":
        foods = manager.list_foods(args.sort)
        for f in foods:
            print(f)
    elif args.command == "get-food":
        food = manager.get_food(args.name)
        if food:
            print(food)
        else:
            print("Food not found.")
    elif args.command == "filter-foods":
        criteria = {}
        if args.gluten_free:
            criteria["gluten_free"] = True
        if args.dairy_free:
            criteria["dairy_free"] = True
        foods = manager.filter_foods(**criteria)
        for f in foods:
            print(f)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
