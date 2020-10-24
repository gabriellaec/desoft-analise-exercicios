def numero_no_indice(lista):
    res = []
    for i, v in enumerate(lista):
        if i == v:
           res.append(v)
    return res