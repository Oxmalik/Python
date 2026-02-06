# Convert the following data into lists using the list() function:

# A tuple: (10, 20, 30)
# A string: "python"
# A range: range(1, 6)
# Print the resulting lists.

# Example Output:

# [10, 20, 30]
# ['p', 'y', 't', 'h', 'o', 'n']
# [1, 2, 3, 4, 5]
# This challenge reinforces using list() to cast different iterables into lists.

tup = (10, 20, 30)
str = "python"
rng = range(1, 6)

tup_lst = list(tup)
str_lst = list(str)
rng_lst = list(rng)

print(f"{tup_lst}")
print(f"{str_lst}")
print(f"{rng_lst}")