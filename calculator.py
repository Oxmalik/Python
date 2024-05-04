#Muhammad Malik
#Calculator
#5/4/2024

print('enter first number')
n1 = int(input()) # Don't change this line
print('enter second number')
n2 = int(input()) # Don't change this line
print('enter operation')
op = input() # Don't change this line
result = 0

if op == '+':
    result=n1+n2
elif op == '-':
    result=n1-n2
elif op == '/':
    result=n1/n2
elif op =='*':
    result=n1*n2
print (result)
