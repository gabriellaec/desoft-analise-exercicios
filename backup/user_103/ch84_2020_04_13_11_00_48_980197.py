def inverte_dicionario(dicionario):
    list(dicionario)
    dic_inverte={}
    i=0
    for i in range (len(dicionario)-1):
        dic_inverte[dicionario[i+1]]=dicionario[i]
        i+=1    
    return dic_inverte
        