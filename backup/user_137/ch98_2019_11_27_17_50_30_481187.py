def bairro_mais_custoso(d):
    p = 0
    k = ''
    for key in d:
        if p < d[key]:
            p = d[key]
            k = key
    return k