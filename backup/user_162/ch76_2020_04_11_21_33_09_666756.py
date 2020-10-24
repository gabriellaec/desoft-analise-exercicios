def aniversariantes_de_setembro(d):
    dic_set = {}
    for n, d in d.items():
        if d[4] == 9:
            dic_set[n] = d
    return dic_set
        