def interseccao_chaves(dicio1,dicio2):
    chavesiguais = []
    for k in dicio1.keys():
        if k in dicio2.keys():
            chavesiguais.append(k)
    return chavesiguais