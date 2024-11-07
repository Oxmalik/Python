# Muhammad Malik
# Max Number
# difficulty Easy
# 11/05/2024

'''
Write a function named max that receives two numbers as input and
 returns the bigger number among the two.

For example, let's assume the input is 132 and 154. 
The function should return 154 because it is bigger than 132.'''

def max(n1, n2):
    print('entered max function')

    if n1> n2:
        print('n1 is bigger')
        return n1
    elif n2> n1:
        print('n2 is bigger')
        return n2
    else:
        print(n1)
    
max(4,5)