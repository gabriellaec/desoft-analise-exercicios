def primeiras_ocorrencias (string):
    d = {}
    c=0
    for i in string:
        if i not in d:
            d[i] = c
            c+=1
        else:
            continue
    return d