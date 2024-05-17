#Muhammad Malik
#return
#5/10/2024

"""
Each test case has three inputs.

The first input indicates how many times to do iterations, and the last two inputs are numbers that we will do operations on.

Create a function that receives two arguments and returns the bigger number of the two. if both are equal then return one of them.

Iterate 'iterations' times and for each iteration do:

1. Call the function with num1, num2, and save the result in a variable.
2. Divide the bigger number of the two by 2, and then replace the original larger variable with the new result value.
3. print the new value.  
4. Continue doing it until the program iterated iterations times or one of the numbers is smaller than 2.
"""

#pseudocode
# take 3 inputs
# define a function that returns bigger number
# for loop to iterate calling the function defined
# in the for loop: 
#                  #1. set bigger number = a var, 
#                  #2. divide the number by two until number is number is less than 2 (we can maybe use break to get out of loop)

iterations = int(input())
num1 = int(input())
num2 = int(input())

def bigger(arg1, arg2):
    if arg1 > arg2:
        return arg1
    elif arg2 > arg1:
        return arg2
    elif arg1 == arg2:
        return arg1

def smaller(arg1, arg2):
    if arg1 > arg2:
        return arg2
    elif arg2 > arg1:
        return arg1
    elif arg1 == arg2:
        return arg1

bnum = bigger(num1,num2)
snum = smaller(num1,num2)

for i in range(iterations):
    # bnum = bigger(num1,num2)
    # snum = smaller(num1,num2)
    bnum/=2
    # print(bnum)
    # numnum = bigger(num, snum)
    if bnum > 2:
        bnum = bigger(bnum,snum)
    elif bnum < 2:
        break
    # print(bnum)


print('return from bigger: ',bnum)    