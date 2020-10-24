def aniversariantes_de_setembro (dic):
    dic_setembro = {}
    for nome, data in dic.items():
        mes = data[3] + data[4]
        if mes == '09':
            dic_setembro [nome] = data
    return dic_setembro