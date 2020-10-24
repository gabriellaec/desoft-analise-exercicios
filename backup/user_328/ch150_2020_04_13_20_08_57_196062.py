def calcula_pi(n):
cont = 0
acum = 0.0
d = 1
while cont < n:
acum = acum + (6.0/d) * (-1)**cont
d = d +2
cont = cont + 1
return 4 * acum