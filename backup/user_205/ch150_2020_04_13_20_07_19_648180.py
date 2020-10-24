from math import sqrt 
def calcula_pi(n):
    contador = 1
    somatoria = 0
    while i<=n:
        somatoria += (6/contador**2)
        contador+=1
    return sqrt(somatoria)
     
        