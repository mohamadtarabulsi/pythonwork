# A Dictionary of Similar Objects
favorite_languages = {
    'mo': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'java',
}

language = favorite_languages['mo'].title()
print(f"Mo's favorite language is {language}")

for key, value in favorite_languages.items():
    print(f"\nName: {key}")
    print(f"Favorite Language: {value}")