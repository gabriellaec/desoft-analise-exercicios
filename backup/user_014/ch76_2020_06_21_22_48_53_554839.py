def aniversariantes_de_setembro (dicionario):
    aniversariantes_setembro = {}
    for aniversario in dicionario.values():
        if aniversario[3] == '0' and aniversario[4] == '7':
            aniversariantes_setembro[nome] = aniversario
    return aniversariantes_setembro