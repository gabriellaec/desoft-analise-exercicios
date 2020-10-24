def aniversariantes_de_setembro(dic):
    dix = {}
    a = dic.keys()
    for i in a:
        if dic[i][4] == '7':
            dix[i] = dic[i]
    return dix