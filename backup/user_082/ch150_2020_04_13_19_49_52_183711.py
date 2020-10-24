def calcula_pi(n):
    pi= 0
    for i in range(n - 1):
        pi = (pi + (6/(n**2)))**(1/2)
    return pi