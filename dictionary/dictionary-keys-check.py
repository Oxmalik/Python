# You are managing a dictionary of employee data, 
# where each key is an employee's name and
# the value is their department. Your task is to:

# Check if "Alice" is a key in the dictionary.
# If it exists, print: "Alice is in the company."
# Check if "John" is not a key in the dictionary.
# If it does not exist, print: "John is not in the company."

employees = {"Alice": "HR", "Bob": "Engineering", "Diana": "Marketing"}

if "Alice" in employees:
    print("Alice is in the company.")
if "John" not in employees:
    print("John is not in the company.")