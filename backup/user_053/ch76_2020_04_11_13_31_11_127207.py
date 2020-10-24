def aniversariantes_de_setembro(calendario):
    calendario_setembro = dict()
    for nome, data in calendario.items():
        if data[4] == '9':  # As barras não contam como elementos da string
            calendario_setembro[nome] = data
    return calendario_setembro