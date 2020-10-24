def calcula_preco(km):
    if (km<=200):
        preco = km*0.5
    else:
        d = km - 200
        preco = 200*0.5 + d*0.45
    return preco