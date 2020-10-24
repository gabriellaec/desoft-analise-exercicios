def posicoes_minusculas (s):
    lista = []
    for e in len(s):
        if e.islower() == True:
            lista.append(e)
    return lista