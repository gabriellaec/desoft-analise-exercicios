def aniversariantes_de_setembro(dicionario):
    niver_de_setembro = {}
    for i in dicionario:
        if dicionario[i][3:5] == '09':
            niver_de_setembro[i]=dicionario[i]
    return niver_de_setembro