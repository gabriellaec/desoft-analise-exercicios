def inverte_dicionario(dicionario):
    dic_inverte={}
    listanomes=list(dicionario.keys())
    listavalores=list(dicionario.values())
    i=0
    for listanomes in listavalores:
        dic_inverte[listavalores[i]]=listanomes[i]
        i+=1 
    print (dic_inverte)

        