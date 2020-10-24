def filtra_positivos(lista):
    listadepositivos = []
    i=0
    while i<len(lista):
        if lista[i]>0:
            listadepositivos.append(lista[i])
        i+=1
    return listadepositivos
        