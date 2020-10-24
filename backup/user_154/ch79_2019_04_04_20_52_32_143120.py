def monta_dicionario(lista1, lista2):
    result = {}
    i = 0
    
    while i < len(lista):
        if lista1[i] not in result:
            result[lista1[i]] = lista2[i]
        
    return result