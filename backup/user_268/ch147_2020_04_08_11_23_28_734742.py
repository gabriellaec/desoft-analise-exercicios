def conta_ocorrencias(lista):
    a = len(lista)
    dic= {}
    for i in range(a):
        if not lista[i] in dic:
            dic[lista[i]] = 1
        else:
            dic[lista[i]] += 1
    return dic

def mais_frequente(list):
    dicio = conta_ocorrencias(list)
    L = max(dicio.values())
    for i in dicio:
        if dicio[i] == L:
        return i
        
        