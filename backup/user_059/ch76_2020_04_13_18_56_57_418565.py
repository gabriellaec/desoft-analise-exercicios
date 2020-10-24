def aniversariantes_de_setembro(d):
    nome = list(d.keys())
    aniv = list(d.values())
    d1 = {}
    for i in range(len(aniv)):
        if aniv[i][4] == '9': 
            d1[nome[i]] = aniv[i]
    return d1
