def calcula_pi(n):
    pi2 = 0
    for i in range (1, n+1):
        pi2 += 6/(i**2)
    pi = (pi2)**(1/2)
    return pi
        