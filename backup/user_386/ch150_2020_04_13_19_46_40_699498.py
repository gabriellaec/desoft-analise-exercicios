import math
def calcula_pi(x):
    lista1=[]
    contador = 1
    while contador <= x:
        pi =(6/(contador**2))
        lista.append(pi)
        contador+=1
    return math.sqrt(sum(lista))
print(calcula_pi(10000))