def apaga_repetidos(string):
    listadeusadas=[]
    novalista=[]
    for i in string:
        if i not in listadeusadas:
            listadeusadas.append(i)
            novalista.append(i)
        else:
            novalista.append('*')
    novastring=''.join(novalista)
    return(novastring)






