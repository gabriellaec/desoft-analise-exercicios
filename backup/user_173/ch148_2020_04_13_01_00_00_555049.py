def conta_letras (x):
    dic = {}
    lista = []
    for i in range(len(x)-1):
        lista.append(x[i])
        
    for item in lista:
        dic[item] = lista.count(item)
        
    return dic
        