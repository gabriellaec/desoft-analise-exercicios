def ocorrencias_letras (palavra):
    dic={}
    for i in range(len(palavra)):
        if palavra[i] in dic:
            dic[palavra[i]]+=1
        else:
            dic[palavra[i]]=1
    return dic
