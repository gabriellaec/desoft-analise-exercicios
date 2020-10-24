def calcula_pi (n):
    i = 1
    pi = 0
    while i <= n:
        if n!= 0:
            pi = (pi + 6/i**2)**0.5
        i += 1
    return pi