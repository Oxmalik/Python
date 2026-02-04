# Create a function named calculate_discount that takes two parameters:

# price: The original price of an item (float)
# discount_percentage: The discount percentage (float)
# The function should:

# Calculate the discount amount
# Subtract the discount amount from the original price
# Round the result to 2 decimal places
# Return the final discounted price
# For example, if the original price is $100 and the discount is 20%, the function should return $80.00.

"""
PSEUDOCODE:

1 -> Calculate discount by percentage
2 -> Subtract from original price and round to 2 decimal places
3 -> return result 

"""
prc = float(input())
# print(f"Initial price: {prc}")
perc = float(input())
# print(f"Discount percentage: {perc}")


def calculate_discount(price, discount_percentage):
    disc_amount = price * (discount_percentage/100)
    # print(f"Calculated discount amount: {disc_amount}")


    post_disc = price - disc_amount
    # print(f"Price after discount: {post_disc}")
    rounded_total = round(post_disc,2)
    return rounded_total

result = calculate_discount(prc, perc)
print(result)
