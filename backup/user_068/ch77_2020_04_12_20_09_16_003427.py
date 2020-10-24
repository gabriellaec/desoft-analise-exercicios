def calcula_tempo(a):
    dicionario = {}
    for p, ace in a.items():
        dicionario[p] = ((200/ ace)**(1/2))
    return dicionario
        