# Membership

# You can check whether an element is in the a list or not (in, not in):

# 2 in [1, 2]      # True
# 3 not in [1, 2]  # True
# 3 in [1, 2]      # False

# Challenge

# Easy
# Create a program that receives two lists and prints a 
# new list of all elements that are in the first list but 
# NOT in the second list.

lst1 = input().split(",")
lst2 = input().split(",")

lst3=[]

for num in lst1:
    if num not in lst2:
        lst3.append(num)
    # print(lst3)


print(lst3)