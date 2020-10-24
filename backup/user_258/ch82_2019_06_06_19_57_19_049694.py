def primeiras_ocorrencias(string):
    dic = {}
    pos = 0
    for k in string:
        if k not in dic:
            dic [k] = pos
        pos += 1
    return dic
            