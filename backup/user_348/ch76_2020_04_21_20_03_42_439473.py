def aniversariantes_de_setembro (dicionário):
    dicionário2 = {}
    for nome,data in dicionário.items():
        data = dia/mes/ano
        if mes==9:
            dicionário2['nome'] = data
            return dicionário2