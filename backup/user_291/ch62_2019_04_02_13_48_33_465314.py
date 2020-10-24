def filtra_positivos(lista5):
    i = 0
    lista7 = []
    while i < len(lista5):
        if lista5[i] < 0:
            del lista5[i]
        i += 1 
    return lista5  
      