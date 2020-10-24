def filtra_positivos(lista):
    cont=0
    
    lista_vazia=[]
    while cont<len(lista):
        if lista[cont]>0:
            lista_vazia.append(lista[cont])
            
        cont+=1
    return lista_vazia
            
        