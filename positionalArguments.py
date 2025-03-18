def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(animal_type = 'dog', pet_name = 'titan')
describe_pet(animal_type = 'hamster', pet_name = 'harry')

def describePet(pet_name, animal_type = 'dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describePet(pet_name = 'willie')