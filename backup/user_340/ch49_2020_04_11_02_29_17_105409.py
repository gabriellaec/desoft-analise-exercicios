def  inverte_lista(lista):
    i=0
    while i<len(lista):
        lista[i]=lista[len(lista)-i]
        
        i+=1
    return lista