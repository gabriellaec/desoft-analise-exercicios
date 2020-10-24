def inverte_dicionario(dic):
    result = {}
    
    for key, value in dic.items():
        if value in result:
            lista = result[value]
            lista.append(key)
            result[value] = lista
        else:
            lista = []
            lista.apend(key)
            result[value] = lista
    
    return result