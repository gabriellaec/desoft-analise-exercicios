def separa_trios(lista_nome):
    trios = []
    #separado = lista_nome.split(',')
    for i in range(0,len(lista_nome),2):
        trios.append(lista_nome[i:(i+2)])
    return trios