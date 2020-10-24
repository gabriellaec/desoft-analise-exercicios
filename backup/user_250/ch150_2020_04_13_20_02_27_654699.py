def calcula_pi(n):
    x = 0
    i = 1
    while i < n:
        x += (6/i**2)**(1/2)
    return x