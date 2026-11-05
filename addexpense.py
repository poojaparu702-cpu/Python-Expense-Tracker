from adodbapi.process_connect_string import process
def add_expense(expenses):
    num=int(input("Enter no  of items"))

    for i in range(num):
        item=input("Enter items")
        price=int(input("enter price"))
        category=input("enter category")

    #create dictionary
        expense = { "item": item,
                    "price": price,
                    "category":category
                  }

        expenses.append(expense)

    print("Expense added successfully")

def view_expense(expenses):
    for expense in expenses:
        print(expense)

def total_expense(expenses):
    total=0
    for expense in expenses:
        total+=expense["price"]
    print(total)

def search_expense(expenses):
    category=input("enter category")
    total = 0
    for expense in expenses:
        if expense["category"] == category:

            print(expense["item"])

            total+=expense["price"]
    print(total)


def high_expense(expenses):
    highest=max(expenses,key=lambda expense:expense["price"])
    print(highest['item'],highest['price'])


def category_view_expense(expenses):
    total=0
    category = input("Enter category")
    for expense in expenses:
       if expense["category"] == category:
            total+=expense["price"]
    print(category,total)
