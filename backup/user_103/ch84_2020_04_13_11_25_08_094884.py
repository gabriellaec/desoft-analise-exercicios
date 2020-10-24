def inverte_dicionario(dicionario):
    dic_inverte={}
    listanomes=list(dicionario.keys())
    listavalores=list(dicionario.values())
    i=0
    for i in range (len(dicionario)):
        if listavalores not in dic_inverte:
            dic_inverte[listavalores[i]]=listanomes[i]

    print (dic_inverte)

        