def primeiras_ocorrencias(palavra):
    dic={}
    listapalavra=[]
    listaocorrencia=[]
    for i in range(len(palavra)):
        if palavra[i] not in listapalavra:
            listapalavra.append(palavra[i])
            listaocorrencia.append(i)
    for i in range(len(listapalavra)):
        dic[listapalavra[i]]=listaocorrencia[i]
    return dic
            
            