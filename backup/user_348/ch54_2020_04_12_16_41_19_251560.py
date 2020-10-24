def calcula_fibonacci(n):
    fibonacci = []
    i = 0
    while i < n-2:
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(fibonacci[i])
        i = i + 1
    return fibonacci
        