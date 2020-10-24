def monta_dicionario(listas):
    dicionario={}
    chaves=listas[0]
    valores=listas[1]
    indice=0
    for i in chaves:
        dicionario[i]=valores[indice]