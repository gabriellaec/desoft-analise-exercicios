def calcula_fibonacci(n):
    f=[0]*n
    f[0]=1
    f[1]=1
    lista=[]
    i=2
    while i<len(f):
        f[i]=f[i-2]+f[i-1]
        i+=1
    return f   