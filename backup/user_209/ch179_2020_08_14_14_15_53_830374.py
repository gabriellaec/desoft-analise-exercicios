def posicoes_minusculas (s):
    lista = []
    for e in s:
        if e.islower():
            lista.append(s.islower(e))
    return lista