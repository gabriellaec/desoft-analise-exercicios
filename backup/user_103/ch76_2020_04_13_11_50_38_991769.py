def aniversariantes_de_setembro(dicionario):
    listanomes=list(dicionario.keys())
    listavalores=str(list(dicionario.values()))
    novalista=[]
    i=6
    while i < len(listavalores):
        if listavalores[i]==9:
            novalista.append(listavalores[i-4])
            novalista.append(listavalores[i-3])
            novalista.append(listavalores[i-2])
            novalista.append(listavalores[i-1])
            novalista.append(listavalores[i])
            return ''.join(novalista)
        else:
            i+=12
        
    
    print(novalista)
    print(listavalores[18])