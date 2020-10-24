def numero_no_indice(x):
    for k in x:
        if x[k] != k:
            del x[k]
    return x