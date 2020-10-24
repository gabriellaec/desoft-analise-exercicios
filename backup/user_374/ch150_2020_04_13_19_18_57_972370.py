def calcula_pi(n):
    i = 2
    calcula = 6
    while i <= n:
        calcula += 6/(i**2)
        i += 1
    return calcula**(1/2)
