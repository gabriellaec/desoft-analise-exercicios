def aniversariantes_de_setembro (dicionario):
    dicionario_setembro = {}
    for nome, aniversario in dicionario.items():
        if aniversario[3] and aniversario[4] == '07':
            dicionario_setembro[nome] = aniversario
    return dicionario_setembro

