def verifica_preco(titulo,dicttitulos,dictcores):
    lista=[]
    preco=dictcores[titulo]
    for titulo in dicttitulos:
        if titulo in dictcores:
            dictcores[titulo]=preco
    return preco
    