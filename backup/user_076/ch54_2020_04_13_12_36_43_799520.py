def calcula_fibonacci(n):
    f = [0]*n
    f[0]=1
    f[1]=1
    i=0
    while i<len(f):
        f[i+2] = f[i] +f[i+1]
        i+=1
    return f