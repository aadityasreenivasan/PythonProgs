#waf add with two args. If both are numbers it gives you the sum of two numbers.
#if one of them is string, it gives you the concatenation of the two args

"""def add(a,b):
    if type(a)==type(b):
        return a+b
    if type(a)==str :
        return a+str(b)
    if type(b)==str:
        return str(a)+b
    return a+b 
    
print(add("cr",7))"""

class fraction:
# private data memebers whole, numerator, denominator
    def _init_(self):
        self.__whole = 0
        self.__numerator = 1
        self.__denominator = 1
    # self.reduce()

# constant static public field to hold the symbol that separates a numeratpr from a denominator
__symbol = '/'

# 3 public member functions

def enterFractionValue(self):
    #  self.whole = whole
    #  self.numerator = numerator
    #  self.denominator = denominator
    #  self.reduce()
    #  if self.denominator == 0:
    #  raise ValueError('Denominator cannot be zero')
    #  user input for the values of the fraction

    print("\n \n \n Object created \n \n \n")
    self.whole = int(input('Enter the whole number: '))
    self.numerator = int(input('Enter the numerator: '))
    self.denominator = int(input('Enter the denominator: '))
    if self.denominator == 0:
        print('Denominator cannot be zero')
        self.denominator = int(input('Enter the denominator: '))
    # else :
    #     # self.reduce()

def gcd(self, a, b):
    if a == 0:
        return b
    return self.gcd(b % a, a)


def reduceFraction(self):
    gcd = self.gcd(self.numerator, self.denominator)
    self.numerator = self.numerator // gcd
    self.denominator = self.denominator // gcd



def displayFraction(self):
    if self.whole == 0:
        print(f'\n\nReduced value : {self.numerator}/{self.denominator}')
    else:
        print(f'{self.whole} {self.numerator}/{self.denominator}')

# driver code
# if _name_ == '_main_':
f = fraction()
f.enterFractionValue()
f.reduceFraction()
f.displayFraction()

f2 = fraction()
f2.enterFractionValue()
f2.reduceFraction()
f2.displayFraction()






