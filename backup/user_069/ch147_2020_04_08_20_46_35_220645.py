def conta_ocorrencias (lista):
    dic = {}
    for e in lista:
        if not e in dic:
            dic[e] = 1
        else:
            dic[e] += 1
    return dic

def mais_frequente (lista):