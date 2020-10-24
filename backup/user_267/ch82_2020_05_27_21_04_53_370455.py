def primeiras_ocorrencias(string):
    dicio = dict()
    i = 0
    while i < len(string):
        if string[i] not in dicio:
            dicio['{0}'.format(string[i])] = i
        i += 1
        