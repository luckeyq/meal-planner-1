# Function to display meal options
def display_meal_options():
    print("Meal Options:")
    print("1. Avocado Toast")
    print("2. Grilled Chicken Salad")
    print("3. Spaghetti Bolognese")
    print("4. Greek Yogurt Parfait")
    print("5. Veggie Wrap")
    print("6. Teriyaki Salmon with Rice")
    # Add more meal options as needed

# Dictionary to store meal options and their ingredients
meal_ingredients = {
    "Avocado Toast": ["Whole grain bread", "Avocado", "Cherry tomatoes", "Salt", "Pepper", "Allergy Warning: Gluten"],
    "Grilled Chicken Salad": ["Chicken breast", "Mixed greens", "Cucumber", "Bell peppers", "Balsamic vinaigrette"],
    "Spaghetti Bolognese": ["Spaghetti pasta", "Ground beef", "Tomato sauce", "Onion", "Garlic", "Parmesan cheese", "Allergy Warning: Lactose, Gluten"],
    "Greek Yogurt Parfait": ["Greek yogurt", "Granola", "Mixed berries", "Honey"],
    "Veggie Wrap": ["Whole wheat wrap", "Hummus", "Lettuce", "Carrots", "Cucumber", "Avocado", "Allergy Warning: Gluten"],
    "Teriyaki Salmon with Rice": ["Salmon fillet", "Teriyaki sauce", "Jasmine rice", "Broccoli"]
}

# Function to create a meal plan
def create_meal_plan():
    meal_plan = {}
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        print(f"\n{day}:")
        display_meal_options()
        while True:
            choice = input(f"Choose a meal for {day} (enter meal number): ")
            if choice.isdigit() and 1 <= int(choice) <= len(meal_ingredients):
                meal_name = list(meal_ingredients.keys())[int(choice) - 1]
                meal_plan[day] = {"Meal": meal_name, "Ingredients": meal_ingredients[meal_name]}
                break
            else:
                print("Invalid choice. Please enter a valid meal number.")
    return meal_plan

# Function to display meal plan
def display_meal_plan(meal_plan):
    print("\nYour Meal Plan:")
    for day, details in meal_plan.items():
        print(f"\n{day}: {details['Meal']}")
        print("Ingredients:")
        for ingredient in details["Ingredients"]:
            print("-", ingredient)

# Main function
def main():
    print("Welcome to the Meal Planner!\n")
    meal_plan = create_meal_plan()
    display_meal_plan(meal_plan)

if __name__ == "__main__":
    main()