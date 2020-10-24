def zera_negativos(lista_numeros):
    i=0
    lista_numeros=[]
    while i<len(lista_numeros):
        if lista_numeros[i]<=0:
            lista_numeros[i]=0
       	i+=1
    return lista_numeros