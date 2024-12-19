# Muhammad Malik
# Factorial
# difficulty Easy
# 12/19/2024


'''Write a function named fact that gets num and 
returns the factorial of num.

Examples,

Factorial of 6 (6!)  ->  1 * 2 * 3 * 4 * 5 * 6 = 720
Factorial of 3 (3!)  ->  1 * 2 * 3 = 6'''

def fact(num):
    if num <= 1:
        return 1
    return num * fact(num -1)
 