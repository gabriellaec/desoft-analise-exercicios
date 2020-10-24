def fatorial(n):
    i=1
    n_fat=n
    while(i<=n):
        fat=(n-i)*n_fat
        n_fat=fat
        i+=1
    return fat