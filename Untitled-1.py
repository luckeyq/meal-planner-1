# Function to display meal options
def display_meal_options():
    print("Meal Options:")
    print("1. Avocado Toast")
    print("2. Grilled Chicken Salad")
    print("3. Spaghetti Bolognese")
    print("4. Greek Yogurt Parfait")
    print("5. Veggie Wrap")
    print("6. Teriyaki Salmon with Rice")


# Dictionary to store meal options, their ingredients, nutritional info, and recipe instructions
meal_data = {
    "Avocado Toast": {
        "Ingredients": ["Whole grain bread", "Avocado", "Cherry tomatoes", "Salt", "Pepper"],
        "Allergies": ["None"],
        "Nutritional Info": {"Calories": 250, "Protein": 8, "Carbs": 20, "Fat": 15},
        "Instructions": "Toast the bread, mash the avocado, spread it on toast, top with sliced cherry tomatoes, salt, and pepper."
    },
    "Grilled Chicken Salad": {
        "Ingredients": ["Chicken breast", "Mixed greens", "Cucumber", "Bell peppers", "Balsamic vinaigrette"],
        "Allergies": ["None"],
        "Nutritional Info": {"Calories": 350, "Protein": 25, "Carbs": 15, "Fat": 20},
        "Instructions": "Grill the chicken breast, chop it and mix with mixed greens, sliced cucumber, and bell peppers. Drizzle with balsamic vinaigrette."
    },
    "Spaghetti Bolognese": {
        "Ingredients": ["Spaghetti pasta", "Ground beef", "Tomato sauce", "Onion", "Garlic", "Parmesan cheese"],
        "Allergies": ["Dairy (Parmesan)"],
        "Nutritional Info": {"Calories": 400, "Protein": 20, "Carbs": 30, "Fat": 15},
        "Instructions": "Cook spaghetti pasta. In a separate pan, cook ground beef with onion and garlic, then add tomato sauce. Serve over cooked pasta with grated Parmesan cheese."
    },
    "Greek Yogurt Parfait": {
        "Ingredients": ["Greek yogurt", "Granola", "Mixed berries", "Honey"],
        "Allergies": ["None"],
        "Nutritional Info": {"Calories": 300, "Protein": 15, "Carbs": 35, "Fat": 10},
        "Instructions": "Layer Greek yogurt, granola, and mixed berries in a glass. Drizzle with honey."
    },
    "Veggie Wrap": {
        "Ingredients": ["Whole wheat wrap", "Hummus", "Lettuce", "Carrots", "Cucumber", "Avocado"],
        "Allergies": ["None"],
        "Nutritional Info": {"Calories": 280, "Protein": 10, "Carbs": 30, "Fat": 12},
        "Instructions": "Spread hummus on the wrap, then add lettuce, grated carrots, sliced cucumber, and avocado. Roll it up and serve."
    },
    "Teriyaki Salmon with Rice": {
        "Ingredients": ["Salmon fillet", "Teriyaki sauce", "Jasmine rice", "Broccoli"],
        "Allergies": ["None"],
        "Nutritional Info": {"Calories": 380, "Protein": 30, "Carbs": 25, "Fat": 18},
        "Instructions": "Marinate salmon fillet in teriyaki sauce, then grill or bake. Serve with cooked jasmine rice and steamed broccoli."
    }
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
            if choice.isdigit() and 1 <= int(choice) <= len(meal_data):
                meal_name = list(meal_data.keys())[int(choice) - 1]
                meal_plan[day] = {"Meal": meal_name, "Ingredients": meal_data[meal_name]["Ingredients"],
                                  "Allergies": meal_data[meal_name]["Allergies"],
                                  "Nutritional Info": meal_data[meal_name]["Nutritional Info"],
                                  "Instructions": meal_data[meal_name]["Instructions"]}
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
        print("Allergies:", ", ".join(details["Allergies"]))
        print("Nutritional Info:")
        for key, value in details["Nutritional Info"].items():
            print(f"- {key}: {value}")
        print("Instructions:", details["Instructions"])

# Main function
def main():
    print("Welcome to the Meal Planner!\n")
    meal_plan = create_meal_plan()
    display_meal_plan(meal_plan)

if __name__ == "__main__":
    main()
1