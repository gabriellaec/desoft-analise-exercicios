def aniversariantes_de_setembro (dicionário):
    dicionário2 = {}
    for nome,data in dicionário.items():
        if data[4]==9:
            dicionário2[nome] = data
    return dicionário2