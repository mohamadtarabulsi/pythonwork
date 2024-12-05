# Chapter 5: Exercise 5-2 More Conditional Tests
''' 
* Tests for equality and inequality with strings
* Tests using the lower() method
* Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and
less than or equal to
* Tests using the 'and' keyword and the 'or' keyword
* Test whether an item is in a list
* Test whether an item is not in a list
'''

# 1. Tests for equality and inequality with strings
fruit = "apple"
print(fruit == "apple")  # True
print(fruit == "orange")  # False

# 2. Tests using the lower() method
name = "John"
print(name.lower() == "john")  # True
print(name.lower() == "JOHN")  # False

# 3. Numerical tests for equality and inequality
age = 25
print(age == 25)  # True
print(age != 25)  # False

# 4. Numerical tests for greater than and less than
height = 180
print(height > 160)  # True
print(height < 160)  # False

# 5. Numerical tests for greater than or equal to and less than or equal to
weight = 150
print(weight >= 150)  # True
print(weight <= 140)  # False

# 6. Tests using the 'and' keyword
temperature = 72
print(temperature > 60 and temperature < 80)  # True
print(temperature > 80 and temperature < 100)  # False

# 7. Tests using the 'or' keyword
day = "Saturday"
print(day == "Sunday" or day == "Saturday")  # True
print(day == "Monday" or day == "Tuesday")  # False

# 8. Test whether an item is in a list
favorite_foods = ["pizza", "burger", "pasta"]
print("pizza" in favorite_foods)  # True
print("sushi" in favorite_foods)  # False

# 9. Test whether an item is not in a list
banned_users = ["user123", "user456", "user789"]
print("user999" not in banned_users)  # True
print("user123" not in banned_users)  # False
