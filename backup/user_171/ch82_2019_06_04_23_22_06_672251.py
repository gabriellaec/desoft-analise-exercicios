def primeiras_ocorrencias(string):
    dic={}
    for i in string:
        if i not in dic:
            dic[i]=0
        dic[i]+=1
    return dic