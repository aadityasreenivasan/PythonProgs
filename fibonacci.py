def fibo(x):
    if 0<=x<=1:
        return x
    else:
        xmin1, xmin2=1,0
        res=0
        for i in range(x-1):
            res=xmin1+xmin2
            xmin2=xmin1
            xmin1=res
    return res

for i in range(36):
    print(i,fibo(i))