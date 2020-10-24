def calcula_tempo(dicionario):
    s = 100
    dados_corredores = {}
    for x in dicionario:
        t = ((2*s)/dicionario[x])**(1/2)
        dados_corredores[x] = t
    return dados_corredores