def conta_ocorrencias(l):
    dic = {}
    for i in l:
        dic[i] = l.count(i)
    return dic

def conta_bigramas(l):
    bi = []
    i = 0
    while i < len(l)-1:
        bi.append(l[i] + l[i+1])
        i+=1
    return conta_ocorrencias(bi)