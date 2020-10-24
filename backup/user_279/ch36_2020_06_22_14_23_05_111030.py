def fatorial(n):    
    c = 0
    f = 1
    for c in range (1, n):
        f *= n
        n -= 1
    return f