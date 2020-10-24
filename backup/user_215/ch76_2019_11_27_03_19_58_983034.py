def aniversariantes_de_setembro(dicionario):
    datas = dicionario.values()
    dict_novo = {}
    for i in datas:
        if i[3:5] == "09":
            dict_novo[i] = dicionario[i]
    print(dict_novo)