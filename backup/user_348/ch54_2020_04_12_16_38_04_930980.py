def calcula_fibonacci(n):
    fibonacci = []
    f = []
    i = 0
    while i < n:
        f[i] = f[i-1] + f[i-2]
        fibonacci.append(f[i])
        i = i + 1
    return fibonacci
        
        