#Muhammad Malik
#Fibonacci
#11/30/2024

'''Create a function named fibo that gets an integer i and returns
 the ith fibonacci series number.

The fibonacci series starts from 0 and 1 and each time the ith element
 equals the sum of the i-1th and i-2th elements.

So,

0th - 0
1th - 1
2th - 1 = 0 + 1
3th - 2 = 1 + 1
4th - 3 = 1 + 2
5th - 5 = 2 + 3
6th - 8 = 3 + 5
7th - 13 = 5 + 8
....'''

def fibo(i):
    if(i==0):
        return 0 
    elif(i==1):
        return 1
    else:
        ans = (i-1) + (i-2)
        print('ans: ', ans)
        return ans

fibo(1)