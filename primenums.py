a=int(input('Enter a number\n'))
flag= False
if a>1:
    for i in range(2,a):
        if (a % i) ==0:
            flag= True
            break
if flag:
    print(a,"is not prime")
else:
    print(a,"is a prime number")
