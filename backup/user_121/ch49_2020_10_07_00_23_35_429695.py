def inverte_lista(lista):
    i=0
    lista_nova=[]
    while i<len(lista):
        lista_nova.insert(0, lista[i])
        i+=1
    return lista_nova