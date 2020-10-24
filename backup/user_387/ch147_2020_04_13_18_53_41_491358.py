def conta_ocorrencias(a):
    dic = {}
    for palavra in a:
        if palavra not in dic:
            dic[palavra] = 1
        else:
            dic[palavra]+=1
    return dic

def mais_frequente(a):
    dic = conta_ocorrencias(a)
    freq = 0
    palav = 'puts'
    for k in dic:
        if dic[k] > freq:
            freq = dic[k]
            palav = k
    return palav