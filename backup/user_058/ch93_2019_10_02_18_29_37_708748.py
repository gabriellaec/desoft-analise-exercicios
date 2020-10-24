import numpy
def munchhausen(x):
    lista= list(str(x))
    #casas=len(lista)
    soma=0
    i=0
    for item in lista:
        soma=soma + numpy.prod(lista[i:i+1])
        i+=1
    if soma!=x:
        return False
    if x==1:
        return False
    else:
        return True