def aniversariantes_de_setembro (dicionario):
    aniversariantes_setembro = {}
    for nome, aniversario in dicionario.values():
        if aniversario[3] and aniversario[4] == '07':
            aniversariantes_setembro[nome] = aniversario
    return aniversariantes_setembro