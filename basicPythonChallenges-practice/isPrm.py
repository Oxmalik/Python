# Muhammad Malik
# prime check
# difficulty Easy
# 12/11/2024

'''Write a function named isPrime that gets an integer 
num and returns true if num is a prime number otherwise
 false.'''

#1 define function
#2 check logarithm
#3 return boolean

# def isPrime(num):
#     if(num == 2 or num == 9):
#         return False
#     elif(num == 11):
#         return True
#     elif ((num % num == 0) and (num % 1 == 0) and (num % 2 == 1)):
#         print('True')
#         return True
#     else:
#         print('False')
#         return False
    
# isPrime(1)

from math import sqrt

def isPrime(num):
    if (num <= 1):
        return False
    elif (num == 2):
        return True
    elif ( (int(sqrt(num)) + 1) ):
        return True