def primeiras_ocorrencias(palavra):
    dict = {}
    i = 0
    while i < len(palavra)-1:
        if palavra[i] not in dict:
            dict[palavra] = i
            i += 1
        else:
            i += 1
    return dict
