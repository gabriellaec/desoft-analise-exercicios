def calcula_fibonacci(n):
    i = 2
    y = [0]*n
    y[0] = 1
    y[1] = 1
    if n < 3:
        return y[n-1]
    else:
        while i < n:
            y[i] = y[i-1] + y[i-2]
            i += 1
        return y
        
