def aniversariantes_de_setembro (dicionario):
    dicionario_setembro = {}
    for nome, aniversario in dicionario.items():
        if aniversario[3] == '0' and aniversario[4] == '9':
            dicionario_setembro[nome] = aniversario
    return dicionario_setembro