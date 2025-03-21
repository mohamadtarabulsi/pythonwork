# 6-6 Polling: Use code from favorite_languages
# Make a list of people who should take the favorite languages poll. 
# Include some names that are already in the dictionary and some that are not. 
# Loop through the list of people who should take the poll. If they have already taken the poll, print 
# a message thanking them for responding. If they have not, print a message inviting them to take the poll. 

# A Dictionary of Similar Objects
favorite_languages = {
    'mo': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'java',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
print("\n")

coders = ['mo', 'sarah', 'edward', 'phil', 'abdullah', 'sali', 'khaldoun']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        print(F"{coder.title()}, what's your favorite programming language?")