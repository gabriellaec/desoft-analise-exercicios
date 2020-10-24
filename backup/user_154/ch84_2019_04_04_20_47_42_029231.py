def inverte_dicionario(dic):
    result = {}
    
    for key, value in dic.items():
        lista = []
        
        if value in result:
            lista = result[value]
        
        lista.append(key)
        result[value] = lista
    
    return result