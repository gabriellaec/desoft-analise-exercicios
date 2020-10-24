def calcula_fibonacci(n):
    n+=1
    f=[0]*n
    f[0]=1
    f[1]=1
    x=2
    while x < n:
        f[x]=f[x-1]+f[x-2]
        x+=1
    return f
    print(f)