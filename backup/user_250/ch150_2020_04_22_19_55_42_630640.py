def calcula_pi(n):
    i = 1
    pi = 0
    while i <= n:
        pi = (pi + (6/i**2))
        i += 1
    return pi**(1/2)