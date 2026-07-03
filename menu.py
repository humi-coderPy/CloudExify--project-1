from expense import add_expense, view_expenses, total_expense

def menu():
    while True:
        print("\n========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")