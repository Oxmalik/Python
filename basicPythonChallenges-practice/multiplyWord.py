#Muhammad Malik
#Remove iTh char
#11/28/2024

'''Write a function named mulWord that gets a string s and an integer n 
and returns the string n times with space between each.'''

# create a for loop to loop n times
# append s to a list
# return list

def mulWord (s, n):
    result = []
    for i in range (n):
        result.append(s)
    print('result ', result)
    fresult = " ".join(result)
    print('fresult ', fresult)
    return fresult


mulWord ('cow', 3)