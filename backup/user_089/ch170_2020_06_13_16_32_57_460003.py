def apaga_repetidos(x):
    nova = []
    for e in x:
        if e in nova:
            nova.append("*")
        else:
            nova.append(e)
    novo = novo.join()
    return novo