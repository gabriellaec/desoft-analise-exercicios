def calcula_fibonacci(n):
    fibo = [0]*n
    fibo[0] = fibo[1] = 1
    i = 2
    
    while i<len(fibo):
        fibo[i] = fibo[i-1] + fibo[i-2]
        i += 1
    
    return fibo
