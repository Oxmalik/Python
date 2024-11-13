# Muhammad Malik
# capitalize
# difficulty Easy
# 11/10/2024

'''Write a function named capitalize that gets a string
 (only lower case) and capitalizes it.'''

# first need to split the words from string
# capitalize the first letter
# then put words back into sentence  
# and then return the string

def capitalize(s):
    words = s.split()
    capWords = []


    for word in words:
        capWord = word[0].upper()+word[1:]
        capWords.append(capWord)
    capSentence=' '.join(capWords)

    # capi = s.capitalize()
    print('capSentence',capSentence)
    return capSentence

capitalize('edumacation is a necessity')