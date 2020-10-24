from statistics import *
def calcula_media(lista):
    notas=[]
    for dic in lista:
        for j in dic:
            notas.append(dic[j])
    return mean(notas)
