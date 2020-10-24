import math
def calcula_norma(vetor):
    lista=[]
    for i in vetor:
        lista.append(i**2)
    listasoma=sum(lista)
    return math.sqrt(listasoma)