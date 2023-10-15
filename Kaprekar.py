"""
In mathematics, a natural number in a given number base is a 

p-Kaprekar number if the representation of its square in that base can be split into two parts, where the second part has 

p digits, that add up to the original number.
"""

def print_Kaprekar_nums(start, end):  
   for i in range(start, end ):  
      sqr = i ** 2  
      digits = str(sqr)  
  
      length = len(digits)  
      for x in range(1, length):  
         left = int("".join(digits[:x]))  
         right = int("".join(digits[x:]))  
         if (left + right) == i:  
            print("%s "%(str(i)), end = " ");  
  
print_Kaprekar_nums(1, 100)  