def calcula_tempo(a):
    dicionario = {}
    for p, t in a.items():
        x = 200/ ((t)**2)
        dicionario[p] = x
    return dicionario
        