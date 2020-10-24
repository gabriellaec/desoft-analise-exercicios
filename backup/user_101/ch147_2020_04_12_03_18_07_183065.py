def conta_ocorrencias(lista):
    dic = {}
    for e in lista:
        if e not in dic:
            dic[e] = 1
        else:
            dic[e] += 1
    return dic

def mais_frequente(dic):
    mais = 0
    dicion = conta_ocorrencias(dic)
    for k, e in dicion.items():
        if int(e) > mais:
            mais = int(e)
            palavra = k
    return palavra