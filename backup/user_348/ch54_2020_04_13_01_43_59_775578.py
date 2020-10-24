def calcula_fibonacci(n):
    fibonacci = [1,1]
    i = 2
    while i < n:
        numero = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(numero)
        i = i + 1
    return fibonacci
        