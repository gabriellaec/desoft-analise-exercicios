def calcula_fibonacci(n):
    sequencia_fibonacci = [1, 1]
    i = 0
    while i < (n - 2):
        sequencia_fibonacci.append(sequencia_fibonacci[-2] + sequencia_fibonacci[-1])
        i += 1
    return sequencia_fibonacci