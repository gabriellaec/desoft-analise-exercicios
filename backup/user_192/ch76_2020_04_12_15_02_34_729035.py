def aniversariantes_de_setembro(aniversarios):
    aniver_setembro = dict()
    for nome, data in aniversarios.items():
        if data[4] == '9':
            aniver_setembro[nome] = data
    return aniver_setembro