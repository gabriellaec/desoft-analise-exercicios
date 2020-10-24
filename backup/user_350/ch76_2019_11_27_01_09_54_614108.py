def aniversariantes_de_setembro(dic):
    dicionario = {}
    for k,v in dic:
        if v[3] == 0 and v[4] == 4:
            dicionario[k] = v
    return dicionario