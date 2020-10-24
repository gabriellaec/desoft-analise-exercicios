def primeiras_ocorrencias(x):
    dicio = dict()
    for letra in x:
        if letra in dicio:
            dicio[letra] += 1 
        else:
            dicio[letra] = 1 
    return (dicio)