from file_handler import load_data, save_data


def add_expense():
    data = load_data()

    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    note = input("Enter Note: ")

    expense = {
        "category": category,
        "amount": amount,
        "note": note
    }

    data.append(expense)
    save_data(data)

    print("Expense added successfully!")


def view_expenses():
    data = load_data()

    if len(data) == 0:
        print("No expenses found.")
        return

    print("\n----- All Expenses -----")

    for i, expense in enumerate(data, start=1):
        print(f"\nExpense {i}")
        print("Category:", expense["category"])
        print("Amount:", expense["amount"])
        print("Note:", expense["note"])


def total_expense():
    data = load_data()

    total = 0

    for expense in data:
        total += expense["amount"]

    print("\nTotal Expense =", total)