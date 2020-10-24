def inverte_dicionario(dicionario):
    dic_inverte={}
    listanomes=list(dicionario.keys())
    listavalores=list(dicionario.values())
    i=0
    for i in range (len(dicionario)-1):
        if listavalores[i]==listavalores[i+1]:
            dc_inverte[listavalores[i]]=listanomes[i],listanomes[i+1]
        else:
            dic_inverte[listavalores[i]]=listanomes[i]

    print (dic_inverte)
    print(listanomes)
    print(listavalores)

        