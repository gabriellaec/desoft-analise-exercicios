def calcula_fibonacci(n):
    fib = [1,1]
    i = 2
    while i<n:
        fib.append(fib[i-2]+fib[i-1])
    return fib