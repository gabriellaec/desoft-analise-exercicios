def primeiras_ocorrencias(string):
    dic=dict()
    for i in string:
        dic[i]=string.find(i)
    return dic
        
        