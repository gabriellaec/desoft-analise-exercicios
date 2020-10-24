def inverte_dicionario(dic):
    inverse = dict()
    for key in dic:
        value = dic[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
    