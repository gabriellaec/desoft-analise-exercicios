def calcula_fibonacci(n):
    sequencia = [1, 1]
    i = 1
    while i < n:
        x = sequencia[i] + sequencia[i-1]
        sequencia.append(x)
        i += 1
    return sequencia