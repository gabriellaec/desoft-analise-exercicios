def calcula_pi (n):
    c = n
    s = 0
    while c > 0:
        s += 6/(c**2)
        c -= 1
    return s**(1/2)