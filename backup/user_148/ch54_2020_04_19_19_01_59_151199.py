def calcula_fibonacci(n):
    fibo = [0]*n
    fibo[0] = fibo[1] = 1
    i = 1
    
    while i<n:
        fibo[i+1] = fibo[i] + fibo[i-1]
        i += 1
    
    return fibo
