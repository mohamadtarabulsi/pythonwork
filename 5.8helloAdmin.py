# 5-8 Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print
# a greeting to each user after they log in to a website. Loop through the list. amd print a greeting to each user.

userNames = ['Admin', 'Mo Salem', 'Kareem', 'Lynn', 'Abdullah', 'Sali']

for username in userNames:
    if username == 'Admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
    
# 5-9 No Users: 
userNames2 = []

for username in userNames2:
    if username == 'Admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")