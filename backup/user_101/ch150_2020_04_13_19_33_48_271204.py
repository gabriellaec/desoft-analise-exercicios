def calcula_pi(n):
    nn = n + 1
    d = range(1, nn)
    pi = 0
    for e in d:
        pi += 6/(e**2)
    return pi**(1/2)