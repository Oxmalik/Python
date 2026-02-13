# Create a function named print_employee_details that takes a dictionary employee_data
#  as an argument. The function should loop through the dictionary and print each key-value pair
#  in the format 'key: value'. If the dictionary is empty, t
# he function should print 'No data available'.

# For example, we have a dictionary called employee_data:

# employee_data = {"name": "John", "age": 30, "department": "Sales"}

# Function output:

# name: John

# age: 30

# department: Sales

def print_employee_details(employee_data):
    if not employee_data:
        print("No data available")
    else:
        for key, value in employee_data.items():
            print(f"{key}: {value}")
   

emp_dict = {
    "name": "John", 
    "age": 30, 
    "department": "Sales"
    }
print_employee_details(emp_dict)