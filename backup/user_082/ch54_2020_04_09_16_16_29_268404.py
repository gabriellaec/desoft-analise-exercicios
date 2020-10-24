def calcula_fibonacci (n):
    fib=[0]*n
    fib[0]=1
    fib[1]=1
    i=0
    while (i< n - 2):
        fib[2+i]=fib[0+i]+fib[1+i]
        i += 1
    return fib