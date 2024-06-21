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

iterations = int(input())
num1 = int(input())
num2 = int(input())

def bigger(arg1, arg2):
    if arg1>arg2:
        # print('bval: ',arg1)
        return arg1
    elif arg2>arg1:
        # print('bval: ',arg2)
        return arg2
    elif arg2 == arg1:
        # print('bSameval: ',arg2)
        return arg2
    

for i in range(iterations):
    bVal=bigger(num1, num2)
    # print('bigger value: ', bVal)

    hVal=bVal/2

    if bVal == num1:
        num1 = hVal
    elif bVal == num2:
        num2 = hVal

    print(hVal)
    if (hVal or num1 or num2) <= 2:
        break