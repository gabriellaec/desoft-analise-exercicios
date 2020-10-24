def calcula_pi(n):
    c = 1
    a = 0
    while c <= n:
        a += (6/(c**2))
        c += 1
        pi = (a)**(1/2)
    return pi
        