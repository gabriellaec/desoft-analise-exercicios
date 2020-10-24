def primeira_ocorrencia(palavra):
    dic={}
    cont=0
    while cont<len(palavra):
        if palavra[cont] not in dic:
            dic[palavra[cont]]=cont
        cont+=1
    return dic