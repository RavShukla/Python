
#loop pending program incomplete



expenses = []
def add_expense(expense):
    category=input("Enter expense category: ")
    amount=int(input("enter amount :"))
    expenses.append({"category":category , "amount":amount})

def view_expenses(expense):
     if  not  expenses:
         print("Expense does not exist")

     else :
         for i,e in enumerate(expenses,start=1):
             print(f"{i}.{e["category"]} -> {e['amount']}")

def total_expenses(expenses):
    total=0
    for i,e in enumerate(expenses,start=1):
        total = total + e["amount"]

    print(total)


def category_expenses(expenses):
    for i,e in enumerate(expenses,start=1):
        expenses[i]["category"]=e["category"]


def category_summary():
    if not expenses:
        print("No expenses found")
        return

    summary = {}

    for e in expenses:
        cat = e["category"]
        amt = e["amount"]


