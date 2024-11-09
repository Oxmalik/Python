# Muhammad Malik
# sum of n
# difficulty Easy
# 11/07/2024

'''Write a function named sum that gets a number n and
 returns the sum of the numbers from 1 to n.'''

def sum(n):
    nsum=0
    for i in range(n+1):
        nsum+=i
    print('nsum: ', nsum)

sum(3)