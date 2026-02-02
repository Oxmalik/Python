# Write a Python program that demonstrates the use of placeholder variables in different scenarios:

# Create a loop that iterates 5 times. Use a placeholder variable (an underscore) since the loop variable is not used within the loop. In each iteration, print the word Iteration.
# You have a list of numbers: [10, 20, 30, 40, 50]. Unpack this list into three variables: first, middle, and last. Use a placeholder variable to ignore the second and fourth values. Then, print the values of first, middle, and last.
# Check the test case for the output format!


# Loop 5 times using a placeholder variable

for _ in range(5):
    print("Iteration")
    
# List of numbers
numbers = [10, 20, 30, 40, 50]

# Unpack the list using placeholder variables

first, _, middle, _, last = numbers

# Print the values of first, middle, and last
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")