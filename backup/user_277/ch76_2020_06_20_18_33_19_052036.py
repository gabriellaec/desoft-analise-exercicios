def aniversariantes_de_setembro(dicionario):
    dicionario2 = {}
    for nome in dicionario:
        data = dicionario[nome]
        verificador = data[4]
        if verificador == '9':
            dicionario2[nome] = data
    return(dicionario2)