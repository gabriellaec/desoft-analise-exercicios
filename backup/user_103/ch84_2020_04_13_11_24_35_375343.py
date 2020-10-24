def inverte_dicionario(dicionario):
    dic_inverte={}
    listanomes=list(dicionario.keys())
    listavalores=list(dicionario.values())
    i=0
    for i in dicionario:
        if listavalores not in dic_inverte:
            dic_inverte[listavalores[i]]=listanomes[i]
        else:
            dic_inverte[listavalores]=listanomes
    print (dic_inverte)

        