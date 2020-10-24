def inverte_dicionario(dicionario):
    list(dicionario)
    dic_inverte={}
    for i in range (len(dicionario)):
        dic_inverte[dicionario[i+1]]=dicionario[i]
    print (dic_inverte)
        