def calcula_pi(n):
    cont = 0
    acum = 0.0
    d = (1)**2
    while cont < n:
    acum = acum + (6.0/d) * (-1)**cont
    d = d + 1
    cont += 1
return acum