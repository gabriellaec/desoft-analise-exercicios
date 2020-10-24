def aniversariantes_de_setembro(dicio):
    setem = {}
    for nome,data in dicio.items():
        if data[3]+data[4] == '09':
            setem[nome] = dicio[nome]
    return setem