def verifica_preco(string,dicttitulos,dictcores):
    if string in dicttitulos:
        cor = dicttitulos[string]
        if cor in dictcores:
            preco = dictcores[cor]
            return preco