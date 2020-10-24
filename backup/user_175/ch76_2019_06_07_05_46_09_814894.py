def aniversariantes_de_setembro(dicionario):
    aniversariantes = {}
    for i in dicionario:
        if (dicionario[i][5] == '9'):
            aniversariantes[i] = dicionario[i]
    return aniversariantes