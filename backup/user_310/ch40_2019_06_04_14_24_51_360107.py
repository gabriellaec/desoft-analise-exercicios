def fatorial(n):
    n_fat=n
    i=1
    while i<n:
        n_fat=(n-i)*n_fat
        i+=1
    return n_fat

