expenses = []

while True:

    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter expense name: ")
        amount = int(input("Enter amount: "))

        expenses.append([name, amount])

        print("Expense Added Successfully")

    elif choice == 2:

        print("\nExpenses List:")
        for item in expenses:
            print(item[0], ":", item[1])

    elif choice == 3:

        total = 0

        for item in expenses:
            total = total + item[1]

        print("Total Expense =", total)

    elif choice == 4:

        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
 