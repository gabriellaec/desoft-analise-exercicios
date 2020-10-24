def inverte_dicionario(dicionario):
    novo={}
    for e in dicionario:
        lista=[]
        for i in dicionario:
            if dicionario[i]==dicionario[e]:
                lista.append(i)
        novo[dicionario[e]]=lista
    return novo
                