def posicoes_minusculas (s):
    lista = []
    for e in range(s):
        if e.islower() == True:
            lista.append(e)
    return lista