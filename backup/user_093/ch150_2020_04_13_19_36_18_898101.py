def calcula_pi(n):
    pii = 0
    for i in range (1, n+1):
        pii += 6/(i**2)
    pi = (pii)**(1/2)
    return pi