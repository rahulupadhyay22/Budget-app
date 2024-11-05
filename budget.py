#create a budget tracker that will help you keep track of your expenses and income.
#freatures are 
#Add Expense – Add a new expense with date, amount, and category.
#View Expenses – Display all recorded expenses.
#Show Summary – Calculate total expenses per category.
#Visualize Expenses (Optional) – Pie chart showing expense distribution.


import csv
from datetime import datetime
import matplotlib.pyplot as plt  # Optional for visualization

#ask user to enter the total amount of money they have budgeted for the month.
def get_budget():
    budget = float(input("Enter your budget for the month: "))
    return budget

# Add Expense
def add_expense():
    date= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (eg. Food, Rent, Transport etc): ")
    
    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])
    print("Expense added successfully!")
# View Expenses
def view_expenses():
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S'):<20} {'Amount':<10} {'Category':<10}")
            print("="*30)
            for row in reader:
                print(f"{row[0]:<20} {row[1]:<10} {row[2]:<10}")
    except FileNotFoundError:
        print("No expenses recorded yet!")
# Show Summary
def show_summary():
    categories = {}
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[2]
                amount = float(row[1])
                categories[category] = categories.get(category, 0) + amount
            
            print("\nexpense summary")
            for category, total in categories.items():
                print(f"{category}: ${total}")
    except FileNotFoundError:
        print("No expenses recorded yet!")
# Visualize Expenses
def visualize_expenses():
    categories = {}
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[2]
                amount = float(row[1])
                categories[category] = categories.get(category, 0) + amount
        labels = categories.keys()
        sizes = categories.values()
        
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('Expense Distribution')
        plt.show()
    except FileNotFoundError:
        print("No expenses recorded yet!")
    
# Main function
def main():
    while True:
        print("\nBudget App")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Visualize Expenses")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_summary()
        elif choice == '4':
            visualize_expenses()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
