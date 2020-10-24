def aniversariantes_de_setembro(dicio):
    dicionovo = {}
    for nome, data in dicio.items():
        mes = data[4:5]
        if mes == '9':
            dicionovo[nome] = data
    return dicionovo
