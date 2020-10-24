def filtra_positivos(lista):
    
    valores = list()
    
    for valor in lista:
        if valor > 0: valores.append(valor)
    
    return valores