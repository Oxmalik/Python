# Muhammad Malikj
# String Validation of Username and Password
# 10/29/2024

"""Create a function named change_element that receives 3 arguments:

First arguments is a list
Second argument is an index
Third argument is a new element
The function will return a modified list by changing the element in an index that is stored in the second argument with the value in the third argument.

For example with the following arguments: change_element([1, 2, 3], 0, 9) the function will return [9, 2, 3]"""

def change_element(lst, index, new_element):
    lst[index] = new_element
    print(lst)
    return lst

change_element([1,2,3], 2, 5)