def monta_dicionario(lista1, lista2):
    result = {}
    i = 0
    
    while i < len(lista1):
        result[lista1[i]] = lista2[i]
        
    return result