#Dev: Muhammad Malik
#Program: Basic While Loop
#5/7/2024

#Prompt:
#You are given a code that prints the numbers from 1 to 10 (including).
#Your task is to add if and break statements so that only the numbers from 1 to 5 will be printed, the loop will exit before printing the numbers from 6 to 10.

for i in range(1, 11):
    if i == 6:
        break
    print(i)