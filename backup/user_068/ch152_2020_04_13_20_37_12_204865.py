def verifica_preco(titulo, dicin, dicic):
    for titulo in dicin.keys():
        cor = dicin[titulo]
        for cor in dicic.keys():
            preco = dicic[cor]
            return preco
        
    return preco
