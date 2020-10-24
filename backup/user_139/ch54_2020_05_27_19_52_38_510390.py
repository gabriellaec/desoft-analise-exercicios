def calcula_fibonacci(n):
    if n == 1:
        sequencia = [1]
    elif n == 2:
        sequencia = [1, 1]
    sequencia = [1, 1]
    i = 1
    while i < (n-1):
        x = sequencia[i] + sequencia[i-1]
        sequencia.append(x)
        i += 1
    return sequencia