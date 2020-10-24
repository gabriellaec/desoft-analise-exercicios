def aniversariantes_de_setembro(dicionario):
    dicionario_setembro = {}
    for nome in dicionario:
        if dicionario[nome][4] == "9":
            dicionario_setembro[nome] = dicionario[nome]
    return dicionario_setembro