# 8-4 Large Shirts: Modify the make_shirt() function so that shirts are large by default
# and read I love Python. Make a large shirt and a medium shirt with the default message,
# and a shirt of any size with a different message.

def make_shirt(size = "Large", text = "I love Python."):
    print(f"\nMew new shirt is a {size} and it says {text}")
    
make_shirt()
make_shirt(size = "Medium")
make_shirt(size = "Small", text = "I love programming!")