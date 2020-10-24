def conta_ocorrencias(a):
    dic = {}
    for palavra in a:
        if palavra not in dic:
            dic[palavra] = 1
        else:
            dic[palavra]+=1
    return dic