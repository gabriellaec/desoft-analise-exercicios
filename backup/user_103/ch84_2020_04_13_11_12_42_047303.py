def inverte_dicionario(dicionario):
    dic_inverte={}
    listanomes=list(dicionario.keys())
    listavalores=list(dicionario.values())
    
    for i in range (len(dicionario)):
        if listavalores[i]==listavalores[i+1]:
            dic_inverte[listavalores[i]]=listanomes[i] and listanomes[i+1]
        else:
            dic_inverte[listavalores[i]]=listanomes[i]

            

    print (dic_inverte)

        