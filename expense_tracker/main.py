
from datetime import datetime

class Expense:
    id = 1
    def __init__(self, amount = 0, category = None, date = str(datetime.now().date())):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        Expense.id += 1
    

    def get_expenses(self):
        print(f"Amount: {self.amount}")
        print(f"Category: {self.category}")
        print(f"Date: {self.date}")

    def change_amount(self, amount):
        self.amount = amount
    


def add_expense(amount, category, date = str(datetime.now().date())):
    expense = Expense(amount, category, date)
    expense_list[expense.id] = expense
    print("Expense added successfully")
    return expense

def remove_expense(id):
    expense_list.pop(id)    

def get_total_amount():
    total_amount = 0
    for expense in expense_list.values():
        total_amount += expense.amount
    return total_amount

def get_expenses_by_category(category):
    expenses = []
    for expense in expense_list.values():
        if expense.category == category:
            expenses.append(expense)
    return expenses 

def get_expenses_by_date(date):
    expenses = []
    for expense in expense_list.values():
        if expense.date == date:
            expenses.append(expense)
    return expenses



expense_list = {}
categories = {"Food": 1, "Clothing": 2, "Entertainment": 3, "Other": 4}
while True:
    print("1. Add expense")
    print("2. Remove expense")
    print("3. Get expenses by category")
    print("4. Get expenses by date")
    print("5. Get total amount")
    print("6. Show categories")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        
        amount = int(input("Enter amount: "))
        category = input("Enter category: ")
        expense = add_expense(amount, category)
        print("Expense added successfully")
    elif choice == 2:
        id = int(input("Enter id: "))
        remove_expense(id)
        print("Expense removed successfully")
    elif choice == 3:
        print("1. Food")
        print("2. Clothing")
        print("3. Entertainment")
        print("4. Other")
        category = input("Enter category: ")
        expenses = get_expenses_by_category(category)
        for expense in expenses:
            expense.get_expenses()
    elif choice == 4:
        date = input("Enter date: ")
        expenses = get_expenses_by_date(date)
        for expense in expenses:
            expense.get_expenses()
    elif choice == 5:
        total_amount = get_total_amount()
        print(f"Total amount: {total_amount}")
    
    elif choice == 6:
        print("1. Food")
        print("2. Clothing")
        print("3. Entertainment")
        print("4. Other")
    elif choice == 7:
        break
    else:
        print("Invalid choice")









