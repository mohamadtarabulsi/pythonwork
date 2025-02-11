# 5-6 Stages of Life: Write an if-elif-else chain that determines a person's stage of life. Set a value for age.

age = 22

if age < 2:
    print("You're a baby.")
elif age < 4:
    print("You're a toddler.")
elif age < 13:
    print("You're a kid.")
elif age < 20:
    print("You're a teenager.")
elif age < 65:
    print("You're an adult.")
else:
    print("You're an elder.")