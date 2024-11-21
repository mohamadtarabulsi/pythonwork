# Exercise 4.11 My Pizzas, Your Pizzas
# Start with your program from exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.abs
''' 
* Add a new pizza to the original list.
* Add a different pizza to the list friend_pizzas
* Prove that you have two separate lists. Print the message "My favorite pizzas are: ",
and then use a for loop to print the first list. Print the message "My friend's favorite pizzas are: ", and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list.
'''

pizzas = ['cheese', 'buffalo chicken', 'pineapple', 'margherita']

friend_pizzas = ['cheese', 'buffalo chicken', 'pineapple', 'margherita']

# Adding new pizzas to list
pizzas.append("pepperoni")
friend_pizzas.append("artichoke")

# pizza print statement
print("My favorite pizzas are: ")

# pizza for loop
for pizza in pizzas:
    print(pizza.title())

# friend_pizzas print statement
print("My friend's favorite pizzas are: ")

# friend_pizzas for loop
for pizza in friend_pizzas:
    print(pizza.title())
