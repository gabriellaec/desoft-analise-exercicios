
def conta_ocorrencias(l):
    dic = {}
    for i in l:
        dic[i] = l.count(i)
    return dic

j = ['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']
print(conta_ocorrencias(j))

def mais_frequente(l):
    valores = []
    dic = conta_ocorrencias(l)
    for i in dic.values():
        valores.append(i)
        maximo = max(valores)
        if i == maximo:
            return i