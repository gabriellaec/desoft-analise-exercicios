def primeiras_ocorrencias(palavra):
    dic={}
    pos=0
    for k in palavra:
        if k not in dic:
            dic[k]=pos
        pos+=1   
    return dic