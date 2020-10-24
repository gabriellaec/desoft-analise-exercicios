def calcula_fibonacci(n):
    i = 2
    CF = []
    fib = []
    fib.append(1)
    fib.append(1)
    while max(fib) < n:
        fib[i] = fib[i-1] + fib[i-2]
        i += 1
        CF.append(fib[i+2])
    return CF
   
        