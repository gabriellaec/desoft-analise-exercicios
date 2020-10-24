def aniversariantes_de_setembro(dic):
    dict_novo = {}
    for nome, data in dic.items():
        if data[3] == 0 and data[4] == 9:
            dict_novo[nome] = data
    return dict_novo