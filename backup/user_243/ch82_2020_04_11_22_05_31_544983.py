def  primeiras_ocorrencias(string):
    dic={}
    i=0
    for t in string:
        dic[t]=i
        i+=1
    return dic