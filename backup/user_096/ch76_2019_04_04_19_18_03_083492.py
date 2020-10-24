def aniversariantes_de_setembro(dicionario):
    saida = {}
    for nome,data in dicionario.items():
        if data[4] == '9':
                saida[nome] = data
    return saida