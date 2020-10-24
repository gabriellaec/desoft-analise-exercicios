def fatorial(n):
    n_fat=n
    i=1
    while i<n:
        fat=(n-i)*n_fat
        n_fat=fat
        i+=1
    return n_fat

