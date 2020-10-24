def aniversariantes_de_setembro (dic):
    dic_final = {}
    for nome, data in dic.items():
        if data[4] == '9':
            dic_final[nome] = data

    return dic_final