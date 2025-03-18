# Write a function called describe_city() that accepts the name of a city and its country. 
# The function should print a simple sentence, such as Reyykjavik is in Iceland. 
# Give the parameter for the country a default value. 
# Call your function for three different different cities, at least one not in the default country. 

def describe_city(city, country = "Syria"):
    print(f"\n{city.title()} is a beautiful city in {country.title()}")
    
describe_city('tartus')
describe_city('homs')
describe_city('houston', country = "america")