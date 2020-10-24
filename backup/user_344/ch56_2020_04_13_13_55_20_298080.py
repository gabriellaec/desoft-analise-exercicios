import math as ze_do_jony
def calcula_norma(lista):
    #|v| = (a**2 + b**2 + ... + n**2)**1/2
    lista2 = []
    for i in lista:
        lista2.append(i**2)
    return ze_do_jony.sqrt(sum(lista2))