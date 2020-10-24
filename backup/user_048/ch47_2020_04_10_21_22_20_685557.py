def estritamente_crescente(lista):
    liste=[]
    liste.append(lista[0])
    for n in range(0,len(lista)):
        if lista[n]>liste[-1]:
            liste.append(lista[n])
        else:
            pass
    return liste
            
            