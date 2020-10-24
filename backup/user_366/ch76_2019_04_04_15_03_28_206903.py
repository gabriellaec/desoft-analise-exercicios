def aniversariantes_de_setembro(dici):
    new = dict()
    for k, v in dici.items():
        if v[4] == '9':
            new[k] = v
    return new