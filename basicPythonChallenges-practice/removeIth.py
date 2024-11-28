#Muhammad Malik
#Remove iTh char
#11/24/2024

'''Write a function named remove that gets 
a string and an integer and returns the string without a letter
 in the index corresponding to the integer.'''

def remove(s, i):

    newStr = s[:i] + s[i+1:]
    print('newStr: ', newStr)


    # spltChars = s.split()
    # print( 'spltChars', spltChars)
    
    # tmpStr = []
    # # fnlStr = []

    # tmpStr = spltChars.replace('s','')
    # print('tmpStr: ', tmpStr)

chars='this Is A String'
remove(chars, 1)