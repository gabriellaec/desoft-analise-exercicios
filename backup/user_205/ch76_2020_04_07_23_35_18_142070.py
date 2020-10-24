def aniversariantes_de_setembro(dicionario):
    resultado = {}
    for nome in dicionario.keys():
        for datas in dicionario.values():
            if dicionario[datas] ==  