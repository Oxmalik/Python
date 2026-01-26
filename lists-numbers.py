# Create a program that receives a list of numbers as input and prints a new list that:

# Contains the original list followed by its reverse
# Has the first element of the original list inserted at the beginning and the last element inserted at the end
# Repeats this entire sequence twice
# For example:

# 1 2 3 → [1, 1, 2, 3, 3, 2, 1, 3, 1, 1, 2, 3, 3, 2, 1, 3]

numbers = input().split()
num_len = len(numbers)

new_lst= ([numbers[0]]+numbers+numbers[::-1]+[numbers[num_len-1]])*2
# new_lst= numbers[0]+numbers+numbers.reverse()+numbers+numbers.reverse()+numbers[len-1]

print(new_lst)