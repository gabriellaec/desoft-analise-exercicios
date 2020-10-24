def fatorial(n):
    x = range(1, n+1)
    fat = 1 
    i = 1

    while i <= n:
        fat = fat * i
        i += 1
    return (fat)