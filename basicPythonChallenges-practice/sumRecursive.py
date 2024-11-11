# Muhammad Malik
# sum of n (recursive)
# difficulty Easy
# 11/07/2024

'''Write a function named sum that gets a number n and
 returns the sum of the numbers from 1 to n.'''

nSum=0

def sum(n):
    # nSum=1
    if n<=0:
        return 0
    # n-=1
    print('nSum: ',nSum)
    print('n: ',n)
    return ((n)+sum(n-1))

returnVal = sum(25)
print('returnVal: ', returnVal)