def conta_ocorrencias(lista):
    dic={}
    i = 0
    while i < range(len(lista)):
        if lista[i] in dic:
            dic[lista[i]] += 1
        else:
            dic[lista[i]] = 1
        i += 1
            
print(conta_ocorrencias(['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']))