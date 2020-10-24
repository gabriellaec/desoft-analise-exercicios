def calcula_pi(n):
    p = 1
    a = list(range(n))
    for i in (a):
        p += (6/(i**2))
    p = (p**(1/2))
    return p