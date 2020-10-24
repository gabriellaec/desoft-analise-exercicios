def primeiras_ocorrencias(string):
    a = len(string)
    dic={}
    c = 0
    for i in string:
        if not i in dic:
            dic[i] = c
            c+=1
        else:
            c+=1
    return dic
        
    