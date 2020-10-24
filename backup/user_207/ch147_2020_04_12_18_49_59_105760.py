def mais_frequente (dicio):
    max = 0
    for v in dicio.values():
        if max < v:
            max = v
    for k, v in dicio.items():
        if v == max:
            chave = k
            print (chave)
    return chave