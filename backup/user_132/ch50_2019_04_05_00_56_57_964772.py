def numero_no_indicie(x):
    for k in x:
        if x[k] != k:
            del x[k]
    return x