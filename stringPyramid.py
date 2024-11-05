# Muhammad Malik
# String Pyramid
# difficulty Medium 
# 11/03/2024

'''Each test case has one input - an odd whole number.
Your task is to print n - pyramid using *, here are some examples:

1 - pyramid
*
5 - pyramid
*
***
*****
7 - pyramid
*
***
*****
*******
Input
odd integer n from user
1 <= n < 1000
Tips
Try starting from the small triangles'''

n = int(input())

def pyramid(count):
    for i in range(count+1):
        if i%2 == 1:
            pyramidStr = '*'*i
            print(pyramidStr)

pyramid(n)