def junta_listas(lista):
    i=0
    lista1=[]
    while i<len(lista):
        lista1.extend(lista[i])
        i+=1
    return lista1
        