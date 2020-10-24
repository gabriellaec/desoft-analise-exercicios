def inverte_dicionario(dicionario):
    dicionario2={}
    for i in dicionario:
        if dicionario[i] not in dicionario2:
            dicionario2[dicionario[i]]=i

        else:
            dicionario2[dicionario[i]]+=i

        return dicionario2