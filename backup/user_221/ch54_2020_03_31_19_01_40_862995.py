def calcula_fibonacci(n):
    fibonacci = [0]*n
    if n == 1:
        return [n]
    i = 0
    fibonacci[0] = 1
    fibonacci[1] = 1
    while i < n-2:
        fibonacci[i+2] = fibonacci[i+1] + fibonacci[i]
        i = i + 1
    return fibonacci
