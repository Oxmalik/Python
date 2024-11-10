# Muhammad Malik
# reverse string
# difficulty Easy
# 11/09/2024

'''Write a function named reverse that gets a string as
 input and returns the string reversed.'''

def reverse(s):
    reverseStr=s[::-1]
    print ('reverseStr: ',reverseStr)
    return reverseStr

reverse('USA')