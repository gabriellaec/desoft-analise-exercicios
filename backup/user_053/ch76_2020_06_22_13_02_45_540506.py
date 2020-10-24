def aniversariantes_de_setembro(nome_data):
    setembro = {}
    for nome, data in nome_data.items():
        if data[3:5] == '09':
            setembro[nome] = data
    return setembro