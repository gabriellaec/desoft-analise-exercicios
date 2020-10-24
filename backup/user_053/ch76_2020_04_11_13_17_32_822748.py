def aniversariantes_de_setembro(calendario):
    calendario_setembro = dict()
    for nome, data in calendario.items():
        if data[4] == 0 and data[5] == 9:
            calendario_setembro[nome] = data
    return calendario_setembro