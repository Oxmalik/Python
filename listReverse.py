# Muhammad Malik
# String Validation of Username and Password
# 11/02/2024

'''Write a function named reverse which gets a list of numbers 
as argument and returns the reversed list.'''

def reverse(lst):
    lsta=[]
    vrbl=(len(lst))-1
    for i in range(len(lst)):
        # vrbl=len(lst)
        lsta.append(lst[vrbl])
        vrbl-=1
        print('new list: ',lsta)
    print('new list final: ',lsta)

# print('new list final: ',lsta)

# lstIn =[1, 2, 3]

lstIn= [3, 5, 7, 1, -4, 98]

reverse(lstIn)

