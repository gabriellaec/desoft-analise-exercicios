def calcula_fibonacci(n):
    sequencia =[]
    sequencia [0] = 1
    sequencia [1] = 1
    i = 1
    while i < n:
        x = i + (i - 1)
        sequencia.append(x)
        i += 1
    return sequencia