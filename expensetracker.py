title = "EXPENSE TRACKER"
print(title.center(50,"*"))

print("-----------------------")

expenses=[]

while True:
    print("1.Add an expense")
    print("2.View all expenses")
    print("3.Calculate total expenses")
    print("4.Search expenses by category")
    print("5.Find Highest expense")
    print("6.View category-wise spending")
    print("7.Exit")


    choice = int(input("ENTER CHOICE"))

    if choice == 1:
        from addexpense import add_expense
        add_expense(expenses)

    elif choice == 2:
        from addexpense import view_expense
        view_expense(expenses)

    elif choice == 3:
        from addexpense import total_expense
        total_expense(expenses)

    elif choice == 4:
        from addexpense import search_expense
        search_expense(expenses)

    elif choice == 5:
        from addexpense import high_expense
        high_expense(expenses)

    elif choice == 6:
        from addexpense import category_view_expense
        category_view_expense(expenses)

    elif choice == 7:
        print("Thank you for using expense tracker")
        break