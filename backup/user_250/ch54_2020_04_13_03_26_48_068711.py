def calcula_fibonacci(n):
    fibo = [1, 1]
    i = 2
    if n > 1:
        while i < n:
            prox = fibo[i-1] + fibo[i-2]
            fibo.append(prox)
            i = i+1
        return fibo
    if n == 1:
        fibo = [1]
        return fibo
    if n == 0:
        fibo = []
        return fibo