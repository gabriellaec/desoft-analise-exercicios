def calcula_pi(n):
    i = 1
    pi = 0
    while i <= n+1:
        pi = (pi + (6/i**2))**(1/2)
        i += 1
    return pi