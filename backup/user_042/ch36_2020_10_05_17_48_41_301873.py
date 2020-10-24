def fatorial(n):
    if n == 0:
        return 1
    i = 1
    a = 0
    b = 0
    while i <= n:
        a = i * (i-1)
        b = a * (a-1)
        f = n * b
        i+= 1
        return f 
        
        