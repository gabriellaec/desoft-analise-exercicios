def calcula_fibonacci(n):
    sequencia_fibonacci = []
    sequencia_fibonacci.append(1)
    if(n == 1):
        return sequencia_fibonacci
    else:
        sequencia_fibonacci.append(1)
        i = 2
        num = 0
        while (i < n):
            num = sequencia_fibonacci[i-1]+sequencia_fibonacci[i-2]
            sequencia_fibonacci.append(num)
            i = i + 1

        return sequencia_fibonacci