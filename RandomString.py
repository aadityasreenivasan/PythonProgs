# program to generate the random string in upper and lower case letters.  
import random  
import string  
def Upper_Lower_string(length): # define the function and pass the length as argument  
    # Print the string in Lowercase  
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length))) # run loop until the define length  
    print(" Random string generated in Lowercase: ", result)  
  