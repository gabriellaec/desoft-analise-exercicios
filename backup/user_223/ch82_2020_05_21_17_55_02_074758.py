def primeiras_ocorrencias(s):
    dic={}
    for l in s:
        i=0
        while i < len(s):
            if l not in dic:
                dic[l]=i
            i+=1
    return dic