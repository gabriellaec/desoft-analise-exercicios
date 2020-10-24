def numero_no_indice(numeros):
    lista_nova=[]
    i=0
    while i<len(numeros):
        if numeros[i]==i:
            lista_nova.append(numeros[i])
            i=1
        else:
            i+=1
    return lista_nova
            
