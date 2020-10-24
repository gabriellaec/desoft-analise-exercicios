def conta_letras(texto):
    dic={}
    for i in texto:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic