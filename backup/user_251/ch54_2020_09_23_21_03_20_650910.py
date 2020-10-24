def calcula_fibonacci(n):
    if n == 1:
        return [1]
    elif n == 2:
        return[1, 1]
    i = 0
    while i < n:
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
        i += 1
    return fibonacci