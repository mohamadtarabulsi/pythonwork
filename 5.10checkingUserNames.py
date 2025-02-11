# 5-10 Checking Usernames: Do the following to create a program that stimulates how websites ensure
# that everyone has a unique username.  

current_users = ['mosalem', 'lynn', 'abdullah', 'evan', 'kareem']
new_users = ['Mosalem', 'abduLLah', 'wassef', 'andrew', 'farris']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}. That username is taken.")
    else:
        print(f"Great! {new_user} is still available.")

