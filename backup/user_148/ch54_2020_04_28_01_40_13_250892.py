def calcula_fibonacci(n):
    fibo = []
    x[0] = 1
    x[1] = 1
    i = 2
    while i<n:
        fibo[i] = x[i-1] + x[i-2]
        i += 1
    return fibo
