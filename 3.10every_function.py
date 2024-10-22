# Exercise 3.10
# Using every function I've learned so far
# Functions to use: append(), insert(), pop(), remove(), sort(), sorted(), reverse(), len()

# List of countries
countries = ['Syria', 'Lebanon', 'China', 'America', 'Canada']

# Appending List
countries.append('Russia')
print(countries)

# Using insert()
countries.insert(0, 'United Kingdom')
print(countries)

# getting len() of list
print(len(countries))

# Using pop()
popped_country = countries.pop()
print(popped_country)
print(countries)

# Using remove()
countries.remove('United Kingdom')
print(countries)

# Using sorted()
print(sorted(countries))

#Using sort()
countries.sort()
print(countries)

# Reverse sort()
countries.sort(reverse=True)
print(countries)

# reverse()
countries.reverse()
print(countries)