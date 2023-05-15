def fact(n):
    print('enter number to find factorial\n')
    factorial=1
    if n<0:
        print("factorial cannot be found")
    elif n==0:
        print("Factorial is 1")
    else:
        for i in range(1,n+1):
            factorial*=i

    print("factorial of",n,"is",factorial)

fact(5)

"""
#using lambda
facto=lambda x: 1 if x<=1 else x*facto(x-1)
facto(7)
"""