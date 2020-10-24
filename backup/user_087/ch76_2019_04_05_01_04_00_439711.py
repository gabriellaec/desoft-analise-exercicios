def aniversariantes_de_setembro(dicionario):
    novo_dicionario = {}
    for nome, data in dicionario.items():
        if data[3] == '0' and data[4] == '9':
            novo_dicionario[nome] = data
    return novo_dicionario 