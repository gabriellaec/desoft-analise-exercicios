def interseccao_chaves(dicionario1,dicionario2):
    listafinal=[]
    lista1=[]
    for chaves1 in dicionario1:
        lista1.append(chaves1)
    for chaves2 in dicionario2:
        if chaves2 in lista1:
            listafinal.append(chaves2)
    return listafinal

