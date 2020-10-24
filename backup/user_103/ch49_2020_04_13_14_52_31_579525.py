def inverte_lista(lista):
    lista1=[]
    i=1
    for i in range(len(lista)-1):
        lista1.append(lista[len(lista)-i])
    return lista1
        
        