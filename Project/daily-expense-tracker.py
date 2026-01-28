# DAILY EXPENSE TRACKER PROJECT PYTHON

welcome_message = """Welcome to the Daily Expense Tracker!

Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit"""
# print(welcome_message)
print(welcome_message)

choice=0
expenses=[]

while(choice!=5):
    # print(welcome_message)
    choice=int(input())
    if choice == 1:
        expense_num=float(input())
        expenses.append(expense_num)
        print("Expense added successfully!")
    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        elif len(expenses) >0:
            count = 1
            print("Your expenses:")
            for numbr in expenses:
                print(f"{count}. {numbr}")
                count+=1
    elif choice == 3 and len(expenses) > 0:
        total_exp=0.0
        avg_exp=0.0
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        elif len(expenses) >0:
            for num in expenses:
                total_exp+=num
            
            avg_exp = total_exp/len(expenses)
            print(f"Total expense: {total_exp}")
            print(f"Average expense: {avg_exp}")
    elif choice == 3 and len(expenses) == 0:
        print("No expenses recorded yet.")
    elif choice == 4:
        expenses.clear()
        print("All expenses cleared.")
    elif choice > 5 or choice < 1:
        print("Invalid choice. Please try again.") 
# print(f"secondary {expense_num}")
print("Exiting the Daily Expense Tracker. Goodbye!")
#     print(choice)
# print('while loop exited')
