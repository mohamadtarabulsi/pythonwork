fave_number = 7
message = "My favorite number is: "

print(message, fave_number)


cars = ['camaro', 'charger', 'challenger', 'mustang']
cars.insert(0, 'bmw')
print(cars)
popped_car = cars.pop()
print(cars)
print(popped_car)
print(f"The last car I owned was a {popped_car.title()}")