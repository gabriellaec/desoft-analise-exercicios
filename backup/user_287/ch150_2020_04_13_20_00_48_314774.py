def calcula_pi(n):
    p = 0
    a = list(range(n))
    a.remove(0)
    for j in (a):
        p += (6/(j**2))
    p = (p**(1/2))
    return p