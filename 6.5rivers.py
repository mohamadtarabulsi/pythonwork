# 6-5 Rivers: Make a dictionary containing three major rivers and the country each rivers runs through. 
# One key value pair might be 'nile':'egypt' 

rivers = {
    'Euphrates': 'Syria',
    'Nile': 'Egypt',
    'Mississippi': 'USA',
    'Thames': 'England',
    'Rhine': 'Germany',
}

for k, v in rivers.items():
    print(f"\nThe {k} runs through {v}.")
    print(f"{v}.")
    print(f"{k}.")