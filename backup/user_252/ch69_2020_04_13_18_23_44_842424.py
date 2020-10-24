def junta_listas(lista):
    lista2=[]
    i=0
    while i < len(lista):
        lista2[i]=lista[i]+lista[i-1]
        i+=1
    return lista2
    
    