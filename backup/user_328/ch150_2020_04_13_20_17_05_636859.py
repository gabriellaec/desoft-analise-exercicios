def calcula_pi(n):
    cont = 0
    a = 0.0
    d = (1)**2
    while cont < n: 
        a = a + (6/d)
        d = d + 1
        cont += 1
    return a