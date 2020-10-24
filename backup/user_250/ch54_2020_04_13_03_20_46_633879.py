def calcula_fibonacci(n):
    fibo = [1, 1]
    i = 2
    while i < n:
        prox = fibo[i-1] + fibo[i-2]
        fibo.append(prox)
        i = i+1
    return fibo