def primeiras_ocorrencias(string):
    occur=dict()
    for in in range(len(string)):
        if string[i] not in occur:
            occur[string[i]]=i
    return occur
        