def medias_por_inicial(dicionario):
    dic={}
    for i in dicionario:
        if i not in dic:
            dic[i]=1
        else:
            dic[i] +=1
    max_key = max(dic, key=dic.get)
    return max_key