
# Continuation of Exercises 3.4 and 3.5
# Adding more guests to my list!

guest_list = ['Messi', 'Lauren', 'Ronaldo']
print("Hey! I just found a bigger dinner table. Let's invite more people!")

# Adding new people to my guest list
guest_list.insert(0, 'N. Armstrong')
guest_list.insert(2, 'Neymar Jr.')
guest_list.append('Batman')

# 3.9 Dinner Guests
# Using len() to get list length
print(len(guest_list))

# Sending invitation messages
msg = f"Hey, {guest_list[0]} would you like to come to dinner?"
print(msg)

msg = f"Hey, {guest_list[1]} would you like to come to dinner?"
print(msg)

msg = f"Hey, {guest_list[2]} would you like to come to dinner?"
print(msg)

msg = f"Hey, {guest_list[3]} would you like to come to dinner?"
print(msg)

msg = f"Hey, {guest_list[4]} would you like to come to dinner?"
print(msg)

msg = f"Hey, {guest_list[5]} would you like to come to dinner?"
print(msg)

# Exercise 3.7 Shrinking Guest List:
# My new dinner table won't arrive in time for dinner
# I can only fit two people instead of six

print('Sorry everyone I can only invite two people to dinner! I Apologize.')
# Removing guests from invitation then letting them know they can't come anymore
popped_name1 = guest_list.pop(0)
msg = f"Sorry, {popped_name1}, you are uninvited to my dinner"
print(msg)

popped_name2 = guest_list.pop(1)
msg = f"Sorry, {popped_name2}, you are uninvited to my dinner"
print(msg)

popped_name3 = guest_list.pop(2)
msg = f"Sorry, {popped_name3}, you are uninvited to my dinner"
print(msg)

popped_name4 = guest_list.pop(0)
msg = f"Sorry, {popped_name4}, you are uninvited to my dinner"
print(msg)

# Letting the remaining guests know they can come to dinner
msg1 = f"Hey {guest_list[0]}, you are still invited to dinner!"
print(msg1)

msg2 = f"Hey {guest_list[1]}, you are still invited to dinner!"
print(msg2)

# Deleting last two guests from list then printing list to make sure it is empty
del guest_list[0]
del guest_list[0]

print(guest_list)