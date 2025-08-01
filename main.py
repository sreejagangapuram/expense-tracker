# runs app
import json
from expense import Expense 

def load_expenses():
    try: 
        # opens file and closes when done
        with open("data.json", "r") as file: 
            # reads json file, turns into python data, list of dictionaries
            return json.load(file)
    except FileNotFoundError: 
        return []

# write mode, json.dump() saves expenses list into file, formating indent 4
def save_expenses(expenses):
    with open("data.json", "w") as file: 
        json.dump(expenses, file, indent=4)

# user can add new data, save and remember 
def add_expense(): 
    amount = float(input("Amount: $ "))
    category = input("Category (e.g., food, rent): ")
    note = input("Note (optional): ")
    # making Expense() object with inputs of amount, category, note
    # loading to previous expenses using func 
    # to_dict() turns expense object into a dictonary like expenses 
    # then we append and add expense object rn to expenses from previous
    # use save func to save  
    expense = Expense(amount, category, note)
    expenses = load_expenses()
    expenses.append(expense.to_dict())
    save_expenses(expenses)
    print("✅ Expense saved!\n")

# read part, show user past expenses from file 
def view_expenses(): 
    expenses =  load_expenses()
    # conditional
    if expenses == []: 
        print("No expenses yet.") 
    else: 
        # loop through list 
        for e in expenses: 
            # how access values in a dict and f string 
            print(f"{e['date']} - ${e['amount']} - {e['category']} - {e['note']}")
    
# main menu 
def main(): 
    while True: 
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Quit")
        choice = int(input("Choose an option (1, 2, 3): "))
        if choice == 1: 
            add_expense()
        elif choice == 2: 
            view_expenses()
        elif choice == 3: 
            break 
        else: 
            print("Invalid choice.")

# this means only run main() if this file is being run directly 
if __name__ == "__main__": 
    main()