def calcula_fibonacci(n):
    fibonacci = []
    f = []
    i = 0
    while i < n:
        f[n] = f[n-1] + f[n-2]
        fibonacci.append(f[i])
        i = i + 1
    return fibonacci
        
        