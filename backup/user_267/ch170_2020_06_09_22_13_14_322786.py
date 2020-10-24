def conta_a(texto):
    soma = 0
    i = 0
    while i < len(texto):
        if texto[i] == 'a':
            soma += 1
        i += 1
    return soma
def primeiras_ocorrencias(string):
    dicio = dict()
    i = 0
    while i < len(string):
        if string[i] not in dicio:
            dicio['{0}'.format(string[i])] = i
        i += 1
    return dicio