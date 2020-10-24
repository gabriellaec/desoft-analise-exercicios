def aniversariantes_de_setembro(dicio):
    for nome,data in dicio.items():
        if data[3]+data[4] != '09':
            del dicio[nome]
    return dicio