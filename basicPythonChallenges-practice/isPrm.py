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
    # if (num <= 1):
    #     print('False')
    #     return False
    # elif (num == 2):
    #     print('True')
    #     return True
    for i in range(2, (int(sqrt(num)) + 1) ):
        if (num % i == 0):
            # print('False')
            return False
    return True

isPrime(13)