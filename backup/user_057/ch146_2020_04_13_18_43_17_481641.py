def conta_ocorrencias(lista):
    dic={}
    for i in range(len(lista)):
        if lista[i] in dic:
            dic[lista[i]] += 1
        else:
            dic[lista[i]] = 1
        i += 1
    return dic
            
print(conta_ocorrencias(['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']))