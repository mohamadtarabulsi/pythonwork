# 4.3 Counting to Twenty
# Use a for loop to print the numbers from 1 to 20, inclusive 
numbers = []
for number in range(1, 21):
    numbers.append(number)
    print(numbers)


# 4.4 One Million
# Make a list of numbers for one to one million and then a for loop to print the numbers
one_million = list(range(1, 1000001))
for million in one_million:
    print(million)

# 4.5 Summing a Million 
# Make a list of the numbers from one to one million, using min(), max(), and sum()
million = list(range(1, 1000001))
print(max(million))
print(min(million))
print(sum(million))

# 4.6 Odd Numbers
# Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use for loop
for number in range(1, 21, 2):
    print(number)
    
# 4.7 Threes
# Make a list of the multiples of 3, from 3 to 30. Use for loop 
threes = list(range(3, 33, 3))
for number in threes:
    print(number)

# 4.8 Cubes
# Make a list of the first 10 cubes. Use for loop to print out value of each cube
cubes = list(range(1, 11))
for number in cubes:
    cubes = number ** 3
    print(cubes)
 
# 4.9 Cube Comprehension
# Use a list comprehension to generate a list of the first 10 cubes
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
