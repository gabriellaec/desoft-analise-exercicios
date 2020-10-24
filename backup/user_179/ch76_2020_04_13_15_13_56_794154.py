def aniversariantes_de_setembro (dicionario):
    i = 0
    lista_nomes = []
    lista_datas = list(dicionario.values())
    while i < len(dicionario):
        data = lista_datas[i]
        if data[3] == '0' and data[4] == '9':
            lista_nomes.append(dicionario[i])
            i = i + 1
        else:
            i = i + 1
    return lista_nomes