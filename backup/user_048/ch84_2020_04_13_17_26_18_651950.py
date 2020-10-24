def inverte_dicionario(dic):
    invertido = {}   
    for key, value in dic.items(): 
        if value not in invertido: 
            invertido[value] = [key] 
        else: 
            invertido[value].append(key) 
    return invertido
    