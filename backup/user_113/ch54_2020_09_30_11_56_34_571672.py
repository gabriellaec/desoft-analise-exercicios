def calcula_fibonacci(n):
    f=[0]*n
    f[0]=1
    f[1]=1
    x=2
    while x < (n+1):
        f[x]=f[x-1]+f[x-2]
        x+=1
    print(f)