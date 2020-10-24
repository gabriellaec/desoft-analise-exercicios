def aniversariantes_de_setembro(dic):
    for nome, data in dic.itens():
        if data[4] == '0' and data[5] == 9:
            dicnovo[nome] =  'value'
    return dicnovo