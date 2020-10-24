def aniversariantes_de_setembro(dic):
    for nome in dic.keys():
        if dic[nome][5] != '9':
            dic.pop(nome,dic[nome])
    return dic
            