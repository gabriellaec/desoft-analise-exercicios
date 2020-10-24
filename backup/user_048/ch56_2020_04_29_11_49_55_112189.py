import math
def calcula_norma(lista):
    listr=[]
    for e in lista:
        listr.append(e**2)
    i=math.sqrt(sum(listr))
    return i
