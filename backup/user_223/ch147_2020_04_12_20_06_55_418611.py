def conta_ocorrencias(l1):
    dic={}
    for e in l1:
        if e in dic:
            dic[e]+=1
        else:
            dic[e]=1
    return dic

def mais_frequente(conta_ocorrencias(l1)):
    ocorrencias = [0]
    for n in dic.values():
        if n > ocorrencias[0]:
            del ocorrencias[0]
            ocorrencias.append(n)
    return ocorrencias