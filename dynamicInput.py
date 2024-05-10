#Muhammad Malik
#dynamicInput
#5/9/2024

#Write a program that gets a dynamic number of input values.
#The first input is a number that represents the number of the input values following it. The next input values are whole numbers.
#In the end, print the sum of all the input numbers (not including the first input).

iter = int(input())
s = 0
for i in range (iter):
    print('iter: ', i)
    num = int(input())
    s+=num
    print(f'sum: {s}')
print(f'final sum: {s}')