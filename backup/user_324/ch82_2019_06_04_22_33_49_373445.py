def primeiras_ocorrencias(palavra):
    dic={}
    palavra=[]
    for i in range(len(palavra)):
        dic[palavra[i]]=[i]
    return dic
        