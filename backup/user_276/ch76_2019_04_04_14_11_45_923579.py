def aniversariantes_de_setembro(dic):
    dicnovo = ''
    for nome, data in dic.itens():
        if data[4] == '0' and data[5] == 9:
            dicnovo[nome] =  data
    return dicnovo