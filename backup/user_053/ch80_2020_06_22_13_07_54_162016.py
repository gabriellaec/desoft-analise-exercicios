def interseccao_chaves(dict1, dict2):
    chaves_comum = []
    for k1 in dict1.keys():
        if k1 in dict2.keys():
            k1.append(chaves_comum)
    return chaves_comum