def calcula_pi(n):
    p = 0
    a = list(range(n))
    a.remove(0)
    for i in (a):
        p += (6/(i**2))
    p = (p**(1/2))
    return p