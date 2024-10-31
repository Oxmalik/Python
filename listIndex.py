# Muhammad Malikj
# String Validation of Username and Password
# 10/29/2024


"""Create a function named values that receives a list as an argument and prints all of the items in the list one after the other.

To iterate over a list use the len() function inside the range() function:

my_list = [10, 20, 30, 40, 50]
for i in range(len(my_list)):
    my_list[i] 
This way i will iterate from 0 to len(my_list) (not including) which is exactly all of the list indices."""

def values(lst):
    for i in range(len(lst)):
        x = lst[i]
        print(x)


shopping_list = ['bread', 'eggs', 'milk', 'butter']
values(shopping_list)