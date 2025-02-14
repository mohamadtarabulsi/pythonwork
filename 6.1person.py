# 6-1 Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.
# Print each piece of information stored in the dictionary

person = {'first_name': 'Mohamad', 'last_name': 'Altarabulsi', 'age': 22, 'city': 'Houston'}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-2 Favorite Numbers: Use a dictionary to store people's favorite numbers.
# Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value in your dictionary.

favorite_numbers = {'Farris': 21, 'Ryan': 11, 'Wassef': 22, 'Andrew': 33, 'Kareem': 17}

num = favorite_numbers['Farris']
print(f"Farris' favorite number is {num}.")

num = favorite_numbers['Ryan']
print(f"Ryan's favorite number is {num}.                       ")

num = favorite_numbers['Wassef']
print(f"Wassef's favorite number is {num}.")

num = favorite_numbers['Andrew']
print(f"Andrew's favorite number is {num}.")

num = favorite_numbers['Kareem']
print(f"Kareem's favorite number is {num}.")