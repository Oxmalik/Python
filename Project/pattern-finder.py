# Create a function named find_occurrences that:

# Takes two string arguments: text and pattern
# Counts how many times pattern appears in text, including overlapping occurrences
# Returns a tuple containing:
# A boolean indicating if the pattern was found (True/False)
# The number of occurrences of the pattern
# A list of starting positions where the pattern was found
# For example, if text is "abababab" and pattern is "aba", your function should return (True, 3, [0, 2, 4]), since "aba" appears at positions 0, 2, and 4.

# If the pattern is not found, return (False, 0, []).

# About the pass keyword: You'll see pass in the default code. It's a Python keyword that means "do nothing" and is used as a placeholder when Python requires an indented code block (like inside a function). You should replace pass with your actual function code.

# Pseudocode:

# 1 -> Does a pattern exist?
# check if there's a python function for string compare
# we can start with first character of string compare with the first character of pattern
# basically check each index of text with each pattern

# 2 -> how many times does the pattern re-occur?
# declare an occurences variable and increment each time occurence is true  

# 3 -> indices where pattern started?
# declare a list and append the index at the point where we find the occurence

# TO-DO: CLEAN THE CODE!!!

def find_occurrences(text, pattern):
    # occurence_exist = False
    occurences = 0
    indices = []

    # for index, chr in enumerate(text):
    #     if text[index : index + len(pattern)] == pattern:
    #         # occurence_exist = True
    #         occurences+=1
    #         indices.append(index)
    #         # print (f"index: {index}, found: {occurence_exist}, indices: {indices}")
    #     else:
    #         occurence_exist = False
    #         # print (f"index: {index}, found: {occurence_exist}, indices: {indices}")
    for index in range(len(text)):
        if text[index : index + len(pattern)] == pattern:
            # occurence_exist = True
            occurences+=1
            indices.append(index)
            # print (f"index: {index}, found: {occurence_exist}, indices: {indices}")
        else:
            occurence_exist = False
            # print (f"index: {index}, found: {occurence_exist}, indices: {indices}")
    
    if len(indices) > 0:
        occurence_exist = True
    elif len(indices) <= 0:
        occurence_exist = False
    
    result = occurence_exist, occurences, indices

    return result


# Read input
# text = input()
# pattern = input()

text = "abababab"
pattern = "aba"

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)