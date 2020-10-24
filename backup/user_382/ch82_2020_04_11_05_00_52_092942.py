def primeiras_ocorrencias(word):
    dic = {}
    for i in range(len(word)-1):
        if word[i] not in dic:
            dic[word[i]] = i       
    return dic