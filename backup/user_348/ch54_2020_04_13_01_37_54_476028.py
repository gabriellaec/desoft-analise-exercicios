def calcula_fibonacci(n):
    fibonacci = []
    i = 0
    while i < n-2:
        numero = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(numero)
        i = i + 1
    return fibonacci
        