def inverte_dicionario(dic):
    inverse = dict()
    for key in dic:
        value = dic[key]
        if value not in inverse:
            inverse[value] = [key]
        else:
            inverse[value].append(key)
    return inverse
    