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