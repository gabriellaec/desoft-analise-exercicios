def calcula_fibonacci(n):
    fib=[1,1]
    i=1
    while i<n-1:
        fib.append(fib[i]+fib[i-1])
        i+=1
    return fib
