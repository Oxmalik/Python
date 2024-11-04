# Muhammad Malik
# 11/1/2024
# list operation

'''Write a function named prod which gets a list of numbers as argument and returns the product of 
all the numbers in the list.

Reminder, product is the multiplication of all the numbers, for [1, 2, 3], return 6 = 1 * 2 * 3.'''

def prod(lst):
    prod=1
    for i in range(len(lst)):
        prod*=lst[i]
        print('prod in loop: ', prod)
    print('final prod: ', prod)

# lsa = [1, 2, 3]
# lsa = [-3, 3, 0]
lsa = [1, 4, 4, 2, 4, 98]

prod(lsa)