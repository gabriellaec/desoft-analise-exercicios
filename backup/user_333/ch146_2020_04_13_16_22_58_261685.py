def conta_ocorrencias(lista):
    dic = {}
    palavras=[]
    valores=[]
    for i in range(len(lista)):
        if lista[i] not in palavras:
            palavras.append(lista[i])
            valores.append[1]
        else:
            for e in range(len(palavras)):
                if lista[i]==palavras[e]:
                    valores[e]+=1
    for j in range(len(palavras)):
        dic[palavras[j]]=valores[j]
    return dic
    
                
    