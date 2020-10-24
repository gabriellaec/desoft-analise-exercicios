def calcula_fibonacci(n):
    i = 0
    CF = []
    fib = []
    fib[0] = 1
    fib[1] = 1
    while fib[i] < n:
        fib[i+2] = fib[i] + fib[i+1]
        i += 1
        CF.append(fib[i+2])
    return CF
   
        