def aniversariantes_de_setembro(dic1):
    dic2 = {}
    for k,v in dic1.items():
        if v[4] == '9':
            dic2[k] = v
    return dic2            