def aniversariantes_de_setembro(dicionario):
    dicionario2 = {}
    for i in dicionario:
        verificador = dicionario[i][4]
        if verificador == '9':
            dicionario2[