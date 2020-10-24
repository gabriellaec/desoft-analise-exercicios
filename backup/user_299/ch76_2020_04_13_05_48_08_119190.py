def aniversariantes_de_setembro(dicio):
    dicionovo = {}
    for nome, data in dicio.items():
        mes = data[4:6]
        if mes == '09':
            dicionovo[nome] == data
    return dicionovo
