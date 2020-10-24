def aniversariantes_de_setembro(dicionario1):
    dicionario2 = {}
    for i in dicionario1.keys():
        a = dicionario1[i]
        if a[4] == '9':
            dicionario2[i] = a[0] + a[1]
        else:
            pass
    return dicionario2