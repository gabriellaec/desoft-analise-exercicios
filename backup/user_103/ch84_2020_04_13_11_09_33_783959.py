def inverte_dicionario(dicionario):
    dic_inverte={}
    listanomes=list(dicionario.keys())
    listavalores=list(dicionario.values())
    
    for i in range (len(dicionario)-1):
        dic_inverte[listavalores[i]]=listanomes[i]
    print (dic_inverte)

        