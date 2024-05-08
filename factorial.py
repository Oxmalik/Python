#Muhammad Malik
#Calculator
#5/7/2024

#Prompt
#Write a program that receives one input, an integer, calculates the factorial of the input and prints it.
#For example, for input 5, the output should be 120 because 1 * 2 * 3 * 4  * 5 = 120.

num = int(input())
fact=1
for i in range (1, num+1):
    fact = fact * i 
    #comments for debugging
    print(f'fact: ',fact)
print(f'final fact: ',fact)