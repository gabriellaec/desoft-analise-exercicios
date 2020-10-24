def primeiras_ocorrencias(string):
    dic={}
    e=0
    for i in string:
        if i not in dic:
            dic[i]=e
        	e+=1
    return dic