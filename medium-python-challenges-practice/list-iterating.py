# Iteration means going through elements one by one in a sequence. With lists, we can access each element systematically using different methods.

# The most common way to iterate through a list is using a for loop:

# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(fruit)
# Output:

# apple
# banana
# orange

# Challenge

# Easy
# Create a program that receives a list as input (given), and prints a new list containing only the words longer than 5 characters

lst = input().split(",")

def listCleaner(lsta):
    cleanList=[]
    for element in lsta:
        if len(element)>5:
            # print(f'adding element: {element}')
            cleanList.append(element)
        # else: 
        #     print(f"removing element: {element}")
    # print(f"final list: {cleanList}")
    print(cleanList)



listCleaner(lst)