def  primeiras_ocorrencias(palavra):
    dic={}
    i=0
    for t in palavra:
        if not i in dic:
            dic[t]=i
        i+=1
    return dic
        