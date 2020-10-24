def primeiras_ocorrencias(s):
    dic={}
    for l in s:
        for i in range (len(s)):
            if l not in dic:
                dic[l]=s[i]
    return dic