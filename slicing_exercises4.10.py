# 4.10 Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
''' 
* Print the message "The first three items in the list are: ". Then use a slice to print the first three items from that program's list.
* Print the message "Three items from the middle of the list are: ". Then use a slice to print three items from the middle of the list. 
* Print the message "The last items in the list are: ". Then use a slice to print the last three items in the list. 
'''
# List of food
foods = ['cheesesteak', 'burrito', 'pizza', 'burger', 'poke', 'sushi', 'cannoli', 'grape leaves', 'pecan pie']
# Printing first three in list
print("The first three items in the list are: ")
print(foods[:3])

# Print three items in middle of list
print("Three items from the middle of the list are: ")
print(foods[3:6])

# Printing last three items in list
print("The last items in the list are: ")
print(foods[-3:])