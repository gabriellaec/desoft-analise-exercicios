def aniversariantes_de_setembro(dicionario):
    dicionario_setembro = {}
    for nome in dicionario:
        for data in dicionario[nome]:
            if data[4] == 9:
                dicionario_setembro[nome] = data
    return dicionario_setembro