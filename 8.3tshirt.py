# 8-3 T-Shirt: Write a function called make_shirt() that accepts a size and the text of
# a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments. 

def t_shirt(size, text):
    print(f"The new shirt I bought is a {size} and it says {text}")
    
t_shirt('Large', 'I Love New York!')

def tShirt(size = "Medium", text = "I Love Syria!"):
    print(f"The new shirt I bought is a {size} and it says {text}")
    
tShirt()