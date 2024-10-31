# Muhammad Malik
# functionRecap
# 10/30/2024

"""Write a function named sigma with one argument that represents a number n.

The function will return the sum of all the numbers from 1 to n (including).

For example, for sigma(5), the function will return 15, because 15 = 1 + 2 + 3 + 4 + 5."""

def sigma(n):
    sum = 0
    for i in range(n+1):
        sum+=i
        print('sum inside loop: ', sum)
    print('final sum: ', sum)
    return sum

sigma(8)
