def conta_letras(palavra):
    dict = {}
    i = 0
    while i < len(palavra)-1:
        if palavra[i] not in dict:
            dict[palavra[i]] = 1
            i += 1
        else:
            dict[palavra[i]] += 1
            i += 1
    return dict