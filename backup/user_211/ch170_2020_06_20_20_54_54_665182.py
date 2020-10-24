def apaga_repetidos(string):
    stringminuscula=string.lower()
    listadeusadas=[]
    novalista=[]
    for i in stringminuscula:
        if i not in listadeusadas:
            listadeusadas.append(i)
            novalista.append(i)
        else:
            novalista.append('*')
    novastring=''.join(novalista)
    return(novastring)


