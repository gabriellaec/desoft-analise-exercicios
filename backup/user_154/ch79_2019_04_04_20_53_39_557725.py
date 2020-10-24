def monta_dicionario(lista1, lista2):
    result = {}
    i = 0
    
    while i < len(lista):
        lista = []
        
        if lista1[i] in result:
            lista = result[lista1[i]]
        
        lista.append(key)
        result[lista1[i]] = lista
        
    return result