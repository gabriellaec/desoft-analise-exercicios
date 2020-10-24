def encontra_maximo(lista1,lista2,lista3):
    i=0
    lista=[]
    while i<len(lista1):
        lista.append(max(lista1))
        lista.append(max(lista2))
        lista.append(max(lista3))
        i+=1
    return max(lista)