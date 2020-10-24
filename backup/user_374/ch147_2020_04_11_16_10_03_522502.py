def conta_ocorrencias(l1):
    dic = {}
    for i in l1:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic

def mais_frequente(lista):
    dic2 = conta_ocorrencias(lista)
    
    v = dic2.values()
    k = dic2.keys()
    
    for i in k:
        if dic2[i] == max(v):
            return i
        
        