# Create a function named check_inventory that takes two parameters: inventory (a dictionary where keys are item names and values are quantities) and item (a string representing the item to check). The function should:

# Check if the item exists as a key in the inventory dictionary.
# If the item exists in the inventory (regardless of quantity), return the string: "<item> is in stock. Quantity: <quantity>".
# If the item does not exist as a key in the inventory, return the string: "<item> is not in stock."
# Note: An item is considered "in stock" if it exists in the inventory dictionary, even if its quantity is 0. The function should only check for the presence of the key, not the quantity value.

# slow brute force 
def check_inventory(inventory, item):
    in_stock = False
    for keys, values in inventory.items():
        if keys == item:
            in_stock = True
            key = keys
            value = values 
    if in_stock:
        print(f"{item} is in stock. Quantity: {value}")
    elif not in_stock:
        print(f"{item} is not in stock.")


#fast approach using dictionary function which is a hash map finding value using key
def check_inventory(inventory, item):
    if item in inventory:
        print(f"{item} is in stock. Quantity: {inventory[item]}")
    print(f"{item} is not in stock.")
