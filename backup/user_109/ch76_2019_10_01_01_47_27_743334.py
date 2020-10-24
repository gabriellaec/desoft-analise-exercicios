def aniversariantes_de_setembro(dicionario_de_aniversariantes):
    dic = {}
    for chave, valor in dicionario_de_aniversariantes.items():
        if valor[3:5] == '09':
            dic[chave] = valor

    return dic