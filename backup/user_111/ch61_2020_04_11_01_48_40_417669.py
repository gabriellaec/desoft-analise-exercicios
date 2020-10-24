def filtra_positivos(reais):
    i=0
    lista_nova=[]
    while i<len(reais):
        if reais[i]>0:
            lista_nova.append(reais[i])
        i+=1
    return lista_nova
            