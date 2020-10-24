def separa_trios(lista_nome):
    trios = []
    for i in range(0,len(lista_nome),3):
        trios.append(lista_nome[i:(i+3)])
    return trios