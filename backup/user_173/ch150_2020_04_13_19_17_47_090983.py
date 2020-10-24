def calcula_pi (n):
    i = 0
    pi = 0
    while i < n:
        pi = (pi + (1/i**2))**0.5
        i += 1
    return pi