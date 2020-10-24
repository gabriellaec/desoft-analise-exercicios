def calcula_fibonacci(n):
    sequencia_fibonacci = []
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    else:
        sequencia_fibonacci = [1, 1]
        i = 0
        while i < (n - 2):
            sequencia_fibonacci.append(sequencia_fibonacci[-2] + sequencia_fibonacci[-1])
            i += 1
        return sequencia_fibonacci