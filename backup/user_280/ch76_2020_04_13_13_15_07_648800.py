def aniversariantes_de_setembro(nome_data):
    setembro = {}
    for nome, data in nome_data.items():
        if data[4] == '9':
            setembro[nome] = data
    return setembro
