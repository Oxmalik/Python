# Create a function named update_employee_info that takes three parameters: employee_dict (a dictionary), key (a string), and value. The function should update the employee_dict with the new key and value. If the key already exists, its value should be updated. If the key does not exist, a new key-value pair should be added. The function must return the updated dictionary.

# Important: Make sure to modify the original dictionary and return it. Use the square bracket notation dict[key] = value to add or update entries.

def update_employee_info(employee_dict, key, value):
    employee_dict[key]=value
    print(employee_dict)