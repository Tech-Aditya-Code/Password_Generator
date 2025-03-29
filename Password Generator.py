import random 
import string

print("Aditya's random password generator")

def myPass():
    
    length = int(input("enter length of password"))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    special = string.punctuation

    combine = lower + upper + number + special

    # always return new value
    x = random.sample(combine, length)  

    # string join method
    password ="".join(x)    
    
    print(password)
    
    myPass()            
myPass()
