# A Dictionary of Similar Objects
favorite_languages = {
    'mo': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'java',
}

language = favorite_languages['mo'].title()
print(f"Mo's favorite language is {language}")

for name, language in favorite_languages.items():
    print(f"\nName: {name}")
    print(f"Favorite Language: {language}")
    
friends = ['sarah', 'phil']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
if name in friends:
    language = favorite_languages[name].title()
    print(f"\n{name.title()}, I see you love {language}!")
    
# Looping Through All Values in a Dictionary 
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())