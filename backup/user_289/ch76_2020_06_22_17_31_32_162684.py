def aniversariantes_de_setembro(dicionario):
    dict_setembro = {}
    for nome, data in dicionario.items():
        if data[4] == '9':
            dict_setembro[nome] = data
    return dict_setembro
            