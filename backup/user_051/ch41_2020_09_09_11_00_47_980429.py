def zera_negativos(lista):
    listaz=[]
    i=0
    while len(listaz)<len(lista):
        if lista[i] < 0:
            listaz.append(0)
            i+=1
        else:
            listaz.append(lista[i])
            i+=1
    return listaz
lista=[1,-1,2,-1]
print(zera_negativos(lista))