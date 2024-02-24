import os
import json
from datetime import datetime


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = {}

    def load_data(self):
        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as file:
                data = json.load(file)
                self.expenses = data.get("expenses", [])
                self.categories = data.get("categories", {})

    def save_data(self):
        data = {"expenses": self.expenses, "categories": self.categories}
        with open("expenses.json", "w") as file:
            json.dump(data, file)

    def add_expense(self, amount, description, category):
        date = datetime.now().strftime("%Y-%m-%d")
        self.expenses.append({"date": date, "amount": amount, "description": description, "category": category})
        if category not in self.categories:
            self.categories[category] = 0
        self.categories[category] += amount
        print("Expense added successfully!")

    def view_summary(self, month):
        total_expenses = 0
        print(f"\nSummary for {month}:\n")
        for expense in self.expenses:
            if expense["date"].startswith(month):
                total_expenses += expense["amount"]
                print(f"{expense['date']} - {expense['description']}: Rs {expense['amount']} ({expense['category']})")
        print("\nTotal Expenses: Rs ", total_expenses)

    def view_category_summary(self):
        print("\nCategory-wise Expenditure:\n")
        for category, amount in self.categories.items():
            print(f"{category}: Rs {amount}")


def main():
    expense_tracker = ExpenseTracker()
    expense_tracker.load_data()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter the amount spent: Rs "))
            description = input("Enter a brief description: ")
            category = input("Enter the expense category: ")
            expense_tracker.add_expense(amount, description, category)

        elif choice == "2":
            month = input("Enter the month (YYYY-MM): ")
            expense_tracker.view_summary(month)

        elif choice == "3":
            expense_tracker.view_category_summary()

        elif choice == "4":
            expense_tracker.save_data()
            print("Exiting Expense Tracker. Data saved.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
