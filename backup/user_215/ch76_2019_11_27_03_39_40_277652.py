def aniversariantes_de_setembro(dicionario):
    datas = list(dicionario.values())
    dict_novo = {}
    for i in datas:
        if i[3:5] == "09":
            dict_novo[i] = dicionario[i]
    return dict_novo