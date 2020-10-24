def calcula_pi(n):
    pi = 0
    for i in range(n):
        pi += (6/((n+1)**2))
    pi = pi**(1/2)
    return pi
    