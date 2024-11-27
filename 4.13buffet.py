# 4-13 Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.abs
''' 
* Use a for loop to print each food the restaurant offers. 
* Try to modify one of the items, and make sure that Python rejects tthe change.
* The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and
then use a for loop to print each of the items on the revised menu.
''' 
# Tuple set
buffet = ('Eggs', 'Pancakes', 'Chicken Breast', 'Salmon', 'Burger')

# for loop to print each food the restaurant offers
print("Original Menu: ")
for buffets in buffet:
    print(buffets)

# New tuple set to change first two items on the menu
buffet = ('Chicken Sandwich', 'Talapia', 'Chicken Breast', 'Salmon', 'Burger')

# for loop to print new menu
print("\nModified Menu: ")
for buffets in buffet:
    print(buffets)