# alien.py 
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding New Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
alien_1 = {}

alien_1['color'] = 'red'
alien_1['points'] = 10

print(alien_1)

# Modifying Values in a Dictionary
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

alien_2 = {'x_position': 0, 'y_position': 25, 'speed':'medium'}
print(f"Original position: {alien_2['x_position']}")

# Move Alien to the right
# Determine how far to move the alien based on its current speed
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_2['x_position'] = alien_2['x_position'] + x_increment
print(f"New position: {alien_2['x_position']}")

# Removing Key Value Pairs
alien_3 = {'color': 'blue', 'points': 20}
print(alien_3)

del alien_3['points'] # Deleted key-value pair is deleted permanently
print(alien_3)

