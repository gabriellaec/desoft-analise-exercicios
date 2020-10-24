def conta_ocorrencia(l):
    dic = {}
    for i in l:
        if not i in dic :
            dic[i] = 1
        else:
            dic[i] += 1
    return dic
