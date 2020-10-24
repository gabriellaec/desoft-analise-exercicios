def fatorial(n):
    n = int(n)
    s=1
    fator = n
    while s < n:
        fator = fator*(n-s)
        s+=1
    return s
        