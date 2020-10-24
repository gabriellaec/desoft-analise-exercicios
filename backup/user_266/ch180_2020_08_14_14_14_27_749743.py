def ocorrencias_letras(s):
    dicio={}
    for i in s:
        if not i in dicio.keys():
            dicio[i] = 1
        else:
            dicio[i] += 1
    return dicio