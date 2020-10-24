def aniversariantes_de_setembro(dic):
    for i in dic.values():
        if dic.values()[4] != "9":
            del dic[i]
    return dic