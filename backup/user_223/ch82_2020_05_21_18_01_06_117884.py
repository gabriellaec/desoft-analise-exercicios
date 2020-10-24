def primeiras_ocorrencias(string):
    dic={}
    i=0
    while i < len(string):
        for l in string:
            if l not in dic.keys():
                dic[l]=i
                i+=1
    return dic