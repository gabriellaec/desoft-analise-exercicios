def verifica_preco(string,dicioN,dicioC):
    for chavee,valore in dicioN.items():
        if chavee==string:
            cor=valore
            for chavei,valori in dicioC.items():
                if chavei==cor:
                    preco=valori
                    return preco
    
    