# Create a program that takes two inputs: a string of numbers separated by spaces, and a prefix string. 
# The program should split the number string into individual numbers, add the prefix to each number, 
# then join these modified numbers back into a single string separated by spaces. Finally, print the resulting string.

# 

numbers = input()
prefix = input()


# nums = "123 456 789"
# prfx = "+1"

# def split_join_string(numbers, prefix):
split_numbers = numbers.split()
# print(f"split_numbers: {split_numbers}")
join_list=[]
for number in split_numbers:
    join_num = prefix + number
    # print(f"join_num: {join_num}")
    join_list.append(join_num)
    # print(f"join_list: {join_list}")

join_string = " ".join(join_list)
# print(f"joint_string: {join_string}")
print(join_string)

# split_join_string(nums, prfx)