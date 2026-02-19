# In this challenge, you'll work with a dictionary of student grades to practice essential dictionary operations.

# Follow these steps in order and use the exact print statements shown:

# Create a dictionary named grades with these initial key-value pairs:
# "Alice": 85
# "Bob": 90
# "Charlie": 78
# Print all student names and grades using these exact statements:
# print("Students:", grades.keys())
# print("Grades:", grades.values())
# Add a new student "Diana" with a grade of 92.
# Use the get() method to retrieve Bob's grade, store it in a variable called bobs_grade, and print it using:
# print("Bob's grade:", bobs_grade)
# Remove "Charlie" from the dictionary using the pop() method and then print the updated dictionary using:
# print("Updated grades:", grades)
# Important: Follow the exact sequence and use the exact print statements shown above to match the expected output.

# Expected Output:
# Students: dict_keys(['Alice', 'Bob', 'Charlie'])
# Grades: dict_values([85, 90, 78])
# Bob's grade: 90
# Updated grades: {'Alice': 85, 'Bob': 90, 'Diana': 92}

# Step 1: Create the Grades Dictionary
grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}


# Step 2: Access All Keys and Values
# Print all students and grades
all_students = grades.keys()
all_grades = grades.values()

print(f"Students: {all_students}")
print(f"Grades: {all_grades}")

# Step 3: Add a New Student
# Add Diana with a grade of 92
grades["Diana"] = 92

# Step 4: Retrieve a Student's Grade
# Get Bob's grade using get() method
bob_grade = grades.get("Bob")
print(f"Bob's grade: {bob_grade}")

# Step 5: Remove a Student
# Remove Charlie using pop() method
# Print the updated dictionary

final_dict = grades.pop("Charlie")
print(f"Updated grades: {grades}")