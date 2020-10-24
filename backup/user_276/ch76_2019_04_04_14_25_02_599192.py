def aniversariantes_de_setembro(dic):
    dict_novo = {}
    for nome, data in dic.itens():
        if data[4] == 0 and data[5] == 9:
            dict_novo[nome] = data
    return dict_novo