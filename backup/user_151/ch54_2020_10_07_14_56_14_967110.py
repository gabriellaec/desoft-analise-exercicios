def calcula_fibonacci(n):
    i = 2
    y = [1, 1]
    while i < n:
        y.append(y[i-1] + y[i-2])
        i += 1
    return y
        
