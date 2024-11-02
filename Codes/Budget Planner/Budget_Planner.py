"""
Budget Planner Application

This program allows users to manage their personal budget by tracking income,
categorizing expenses, and saving data to a CSV file for persistence.

Features:
- Set budget amounts for various categories
- Add income and allocate it to categories
- Track spending by category
- View budget summary with allocated and spent amounts
- Save and load budget data from a CSV file

Author: Your Name
Date: YYYY-MM-DD
"""

import csv

# Budget categories with allocated amounts
budget = {
    "Income": 0.0,
    "Food": 0.0,
    "Rent": 0.0,
    "Entertainment": 0.0,
    "Transportation": 0.0,
    "Other": 0.0
}

expenses = {
    "Food": 0.0,
    "Rent": 0.0,
    "Entertainment": 0.0,
    "Transportation": 0.0,
    "Other": 0.0
}

# Load data from file


def load_data(filename="budget.csv"):
    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                category, amount = row
                if category in budget:
                    budget[category] = float(amount)
    except FileNotFoundError:
        print("No existing budget data found. Starting fresh.")

# Save data to file


def save_data(filename="budget.csv"):
    with open(filename, mode="w") as file:
        writer = csv.writer(file)
        for category, amount in budget.items():
            writer.writerow([category, amount])

# Set budget amounts


def set_budget():
    print("Set your budget amounts:")
    budget["Food"] = float(input("Enter budget for Food: "))
    budget["Rent"] = float(input("Enter budget for Rent: "))
    budget["Entertainment"] = float(input("Enter budget for Entertainment: "))
    budget["Transportation"] = float(
        input("Enter budget for Transportation: "))
    budget["Other"] = float(input("Enter budget for Other: "))
    print("\nBudget has been set!\n")

# Add income


def add_income():
    income = float(input("Enter income amount: "))
    budget["Income"] += income
    print(f"Added {income} to income.\n")

# Add expense


def add_expense():
    category = input(
        "Enter expense category (Food, Rent, Entertainment, Transportation, Other): ")
    if category in expenses:
        amount = float(input(f"Enter expense amount for {category}: "))
        if amount <= budget["Income"]:
            expenses[category] += amount
            budget["Income"] -= amount
            print(f"Added expense of {amount} to {
                  category}. Remaining income: {budget['Income']}\n")
        else:
            print("Insufficient funds.")
    else:
        print("Invalid category. Try again.")

# Show budget summary


def show_summary():
    print("\nBudget Summary:")
    print(f"Income available: ${budget['Income']}")
    for category in expenses:
        print(
            f"{category} - Spent: ${expenses[category]}, Allocated: ${budget[category]}")
    print()

# Main program loop


def main():
    load_data()  # Load existing data on start
    set_budget()  # Set budget at the beginning
    print("Welcome to the Budget Planner!")

    while True:
        print("\nOptions:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Save and Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            save_data()  # Save data on exit
            print("Budget saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
