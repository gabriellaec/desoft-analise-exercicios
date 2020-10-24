def calcula_pi(n):
    x = 1
    s = 0
    while x < n+1:
        s += 6/(x**2)
        x += 1
    return s**(1/2)