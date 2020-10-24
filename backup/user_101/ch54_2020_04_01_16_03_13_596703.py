def calcula_fibonacci(n):
    fib = [1] * n
    i = 2
    while i < n:
        fib[i] = fib[i-1] +fib[i-2]
        i += 1
    return fib