def calcula_fibonacci(n):
    fib = []
    i = 0
    while i<n and i<2:
        fib.append(1)
        i+=1
    while i<n:
        fib.append(fib[i-2]+fib[i-1])
        i+=1
    return fib