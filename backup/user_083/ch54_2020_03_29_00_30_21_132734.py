def fibonacci(x):
    f=[0]*x
    f[0]=1
    f[1]=1
    i=0
    while x>0:
        f[i]=f[i-1]+f[i-2]
        i+=1
    print(fibonacci(9))