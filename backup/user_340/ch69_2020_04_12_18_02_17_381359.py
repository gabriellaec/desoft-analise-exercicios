def junta_listas(lista):
    lista1=[]
    i=0
    while i<len(lista):
        for t in lista[i]:
            lista1.append(t)
        i+=1
    return lista1