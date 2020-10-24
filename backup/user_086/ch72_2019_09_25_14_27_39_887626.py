def lista_caracteres(string):
    listacaract=[]
    i=0
    while i<len(string):
        if not string[i] in listacaract:
            listacaract.append(string[i])
            i+=1
    return listacaract