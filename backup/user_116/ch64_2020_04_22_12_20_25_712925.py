def acha_bigramas(stri):
    lista=[]
    for n in range(0,len(stri)-1):
        if stri[n]+stri[n+1] not in lista:
            lista.append(stri[n]+stri[n+1])
    return lista
