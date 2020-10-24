def filtra_positivos(lista):
    cont=0
    contador=0
    lista_vazia=[]
    while cont<len(lista):
        if lista[cont]>0:
            lista_vazia.append(lista[cont])
            contador+=1
        cont+=1
    return lista_vazia
            
        