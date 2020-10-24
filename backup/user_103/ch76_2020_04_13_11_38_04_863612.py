def aniversariantes_de_setembro(dicionario):
    listanomes=list(dicionario.keys())
    listavalores=str(list(dicionario.values()))
    novalista=[]
    i=6
    while i < len(listavalores):
        if listavalores[i]==9:
            novalista.append(listavalores[i])
        else:
            i+=12
        
    
    print(novalista)