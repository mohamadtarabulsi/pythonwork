# 5-4 Alien Colors #2
# Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
''' * If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien
* If the alien's color isn't green, print a statement that the player just earned 10 points.
* Write one version of this program that runs the if block and another that runs the else block. '''

alien_color = "green"
# if-else statement testing whether color is green or not
if alien_color == "green":
    print("Congratulations! You earned 5 points for shooting the alien.")
else:
    print("The alien is not green. You just earned 10 points!")
    
# New program that run the 'else' block
alien_color2 = "red"

if alien_color2 == "green":
    print("Congratulations! You earned 5 points for shooting the alien.")
else:
    print("The alien is not green. You just earned 10 points!")
    
### 5-5 Alien Colors #3 
# Turn your if-else chain from exercise 5-4 into an if-elif-else chain.
""" * If the alien color is green, print a message that the player earned 5 points.
* If the alien is yellow, print a message that the player earned 10 points.
* If the alien is red, print a message that the player earned 15 points.
* Write three versions of this program, making sure each message is printed for the appropriate color alien. """

# green if elif else statement
if alien_color == "green":
    print("Alien is green. You just earned 5 points.")
elif alien_color == "yellow":
    print("Alien is yellow. You just earned 10 points.")
else:
    print("Alien is red. You just earned 15 points.")

# yellow if elif else statement
alien_color3 = "yellow"

if alien_color3 == "green":
    print("Alien is green. You just earned 5 points.")
elif alien_color3 == "yellow":
    print("Alien is yellow. You just earned 10 points.")
else:
    print("Alien is red. You just earned 15 points.")
    
# red if elif else statement
if alien_color2 == "green":
    print("Alien is green. You just earned 5 points.")
elif alien_color2 == "yellow":
    print("Alien is yellow. You just earned 10 points.")
else:
    print("Alien is red. You just earned 15 points.")
    
