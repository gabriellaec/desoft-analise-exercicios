def  inverte_lista(lista):
    i=0
    while i<len(lista):
        lista[i+len(lista)-1]=lista[i]
        i+=1
    return lista