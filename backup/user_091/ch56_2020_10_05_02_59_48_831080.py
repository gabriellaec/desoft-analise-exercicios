import math
def calcula_norma(lista):
    soma=0
    i=0
    while i<len(lista):
        soma+=(lista[i])**2
        i+=1
    return math.sqrt(soma)
    
    