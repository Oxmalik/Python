# Each test case has one input - an odd whole number (always odd, given).
# Your task is to print n - pyramid using *, here are some examples:

# 1 - pyramid
# *
# 5 - pyramid
# *
# ***
# *****
# 7 - pyramid
# *
# ***
# *****
# *******
# Input
# odd integer n from user
# 1 <= n < 1000

n = int(input())

astrik = "*"
count = 1
for i in range((n+1)//2):
    print(astrik*count)
    count+=2