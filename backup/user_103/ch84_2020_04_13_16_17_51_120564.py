def inverte_dicionario(dicionario):
    dic_inverte={}
    listanomes=list(dicionario.keys())
    listavalores=list(dicionario.values())
    i=0
    for i in range (len(listavalores)):
        if listavalores[i]==listavalores[i+1]:
            dic_inverte[listavalores[i]]=listanomes[i],listanomes[i+1]
        else:
            dic_inverte[listavalores[i]]=listanomes[i]

    print (dic_inverte)
    print(listanomes)
    print(listavalores)

        