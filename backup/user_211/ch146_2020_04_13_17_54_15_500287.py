def conta_ocorrencias(lista):
    dic={}
    w=0
    for k,v in lista.items():
        dic[k].append(v)
        w+=1
    return { i: w for i,j in dic.items()}
    