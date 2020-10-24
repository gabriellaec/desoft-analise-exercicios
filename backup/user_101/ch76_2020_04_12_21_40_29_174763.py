def aniversariante_de_setembro(dic):
    dic9 = {}
    for k, v in dic.items():
        if v[4] == 9:
            dic9[k] = v
    return dic9