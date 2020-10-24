def posicoes_minusculas (s):
    lista = []
    for e in s:
        if e.islower():
            lista.append(s.index(e))
    return lista