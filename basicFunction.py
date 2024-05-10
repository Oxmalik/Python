#Muhammad Malik
#basicFunction
#5/9/2024

'''
Write a program that gets one input, a number. The input number indicates how many times to execute the below function. 

Create a function that calculates the sum of all of the numbers between 1 and 10000 (including) and prints it, name the function however you like.
'''

def addition():
    s = 0
    for i in range(1,10001):
        s+=i
    print(s)

iter = int(input())
for i in range (iter):
    #print('iter: ', i)
    addition()  