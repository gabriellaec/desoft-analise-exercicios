def filtra_positivos(lista):
    result = []
    
    for x in lista:
        if x >= 0:
            result.append(x)
    
    return result