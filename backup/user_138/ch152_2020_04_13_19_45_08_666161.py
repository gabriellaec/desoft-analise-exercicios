def verifica_preco(string,dicttitulos,dictcores):
    if string in dicttitulos:
        if string in dictcores:
            return dictcores.values()