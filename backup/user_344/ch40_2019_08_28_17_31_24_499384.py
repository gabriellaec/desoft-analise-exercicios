def fatorial(n):
    res = 1
    n_fat=n
    while n_fat>1:
        res *= n_fat
        n_fat-=1
    return res
