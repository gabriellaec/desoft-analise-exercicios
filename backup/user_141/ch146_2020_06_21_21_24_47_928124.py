
def conta_ocorrencias(lista):
    dic = {}
    for palavras in lista:
        if palavra not in dic:
            disc[palavra] = 1
        else:
            dic[palavra]+=1
    return dic
    