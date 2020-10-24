def conta_letras (x):
    dic = {}
    lista = []
    for i in range(len(s)-1):
        lista.append(s[i])
        
    for item in lista:
        dic[item] = lista.count(item)
        
    return dic
        