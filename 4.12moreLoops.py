# 4-12 More Loops
# All versions of foods.py in this section have avoided using for loops when printing, to save space
# Choose a version of foods.py, and write two for loops to print each list of foods

pizzas = ['cheese', 'buffalo chicken', 'pineapple', 'margherita']

friend_pizzas = ['cheese', 'buffalo chicken', 'pineapple', 'margherita']

# Adding new pizzas to list
pizzas.append("pepperoni")
friend_pizzas.append("artichoke")

# Loop to print pizzas
print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")

# Loop to print friend's pizzas
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(f"- {friend_pizza}")