def filtra_positivos(lista):
    i = 0
    lista_positiva = []
    while i < len(lista):
        if lista[i]>0:
            lista_positiva.append(lista[i])
        i+=1
    return lista_positiva
            
   
        