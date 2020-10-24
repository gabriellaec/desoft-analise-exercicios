lista=[4,3,-1,-5,0]

def negativo(lista):
    i=0
    while i<len(lista):
        if lista[i]<0:
            lista[i]= 0
        i+=1
    return lista
print(negativo(lista))