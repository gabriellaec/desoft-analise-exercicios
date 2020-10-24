def junta_listas(lista):
    i=0
    lista1=[]
    while i<len(lista):
        for t in lista[i]:
            lista1.append(t)
        i+=1
    return lista1