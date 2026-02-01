# Write a program that receives three inputs (given):

#  A list of prices
# A list of item names
# A budget per item
 

# The program should print:

# A list of items that you can afford within your budget
# How much budget would you need if you bought all of the affordable items
# How many items you couldn't afford

# pseudocode:

"""
1 -> LIST OF AFFORDABLE ITEMS:
   - compare budget with each price in price list
   - for each price <= budget append item in that item list to affordable items list
   - return affordable list

2 -> Total Budget Needed:
    - For each affordable item add all the prices
    - return int total budget

3 -> Un-Affordable Items Count:
    - each item thats more than the budget then count++
"""

prices = input().split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input().split(",")
budget_per_item = int(input())

affordable_items = []
cant_afford = 0
total_needed = 0
unaffordable_items=[]
affordable_items_index=[]



# print(f"prices: {prices}, items: {items}, budget_per_item: {budget_per_item}")

for index, num in enumerate(prices):
    if num <= budget_per_item:
        affordable_items.append(items[index])
        total_needed+=num
    elif num > budget_per_item:
        unaffordable_items.append(items[index])

cant_afford=len(unaffordable_items)


# Write your code below




print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)