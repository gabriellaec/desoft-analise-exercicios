def aniversariantes_de_setembro (dicionario):
    lista_aniversariantes = []
    lista_nomes = list(dicionario.keys())
    lista_datas = list(dicionario.values())
    i = 0
    for i in dicionario:
        data = lista_datas[i]
        if data[3] == '0' and data[4] == '9':
            lista_aniversariantes.append(lista_nomes[i])
    return lista_aniversariantes