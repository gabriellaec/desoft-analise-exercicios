def aniversariantes_de_setembro (dic):
    dic_setembro = {}
    for nome, data in dic.items():
        mes = data[4] + data[5]
        if mes == '09':
            dic [nome] = data
        else:
            dic = []
    return dic_setembro