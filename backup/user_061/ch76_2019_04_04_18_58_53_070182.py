def aniversariantes_de_setembro(dicionario):
    setembrinos = {}
    for nome in dicionario:
        if dicionario[nome][4] == "9":
            setembrinos[nome] = dicionario[nome]
    return setembrinos