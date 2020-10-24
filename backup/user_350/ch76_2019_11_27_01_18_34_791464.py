def aniversariantes_de_setembro(dic):
    dicionario = {}
    for name in dic:
        if name[3] == 0 and name[4] == 9:
            dicionario[name] = name
    return dicionario