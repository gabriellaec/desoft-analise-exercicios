def conta_ocorrencias(l):
    dic = {}
    for i in l:
        dic[i] = l.count(i)
    return dic

def mais_frequente(l):
    valores = []
    dic = conta_ocorrencias(l)
    
    for i in dic:
        valores.append(i)
        maximo = max(valores)
        if i == maximo:
            return i
        