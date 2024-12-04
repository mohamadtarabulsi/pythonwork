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

# Test for equality with strings
fruit = "apple"
print(fruit == "apple")  # True

# Test for inequality with strings
color = "blue"
print(color != "red")  # True

# Test using the lower() method
name = "John"
print(name.lower() == "john")  # True

# Numerical test for equality
age = 25
print(age == 25)  # True

# Numerical test for inequality
temperature = 72
print(temperature != 68)  # True

# Numerical test for greater than and less than
height = 180
print(height > 160 and height < 200)  # True

# Numerical test for greater than or equal to
weight = 150
print(weight >= 150)  # True

# Test using the 'or' keyword
day = "Saturday"
print(day == "Sunday" or day == "Saturday")  # True

# Test whether an item is in a list
favorite_foods = ["pizza", "burger", "pasta"]
print("pizza" in favorite_foods)  # True

# Test whether an item is not in a list
banned_users = ["user123", "user456", "user789"]
print("user999" not in banned_users)  # True
