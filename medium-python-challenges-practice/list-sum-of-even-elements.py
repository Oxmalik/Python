# Create a program that receives a list of numbers as input (given), and prints the sum of all even numbers in the list.

# numbers = input().split(",")
numbers=[13,24,35,46,57,68]

def summation(numbersa):
    numberSum=0
    for element in numbersa:
        num=int(element)
        if (num%2 ==0):
            # print(f'adding element: {element}')
            numberSum += num
    #     else: 
    #         print(f"not adding element: {element}")
    # print(f"final sum: {numberSum}")
    print(numberSum)

summation(numbers)