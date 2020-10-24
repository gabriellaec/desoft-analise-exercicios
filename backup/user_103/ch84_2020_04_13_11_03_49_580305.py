def inverte_dicionario(dicionario):
    dic_inverte={}
    i=0
    for i in range (len(dicionario)-1):
        dic_inverte[dicionario.values()]=dicionario.keys()
    print (dic_inverte)

        