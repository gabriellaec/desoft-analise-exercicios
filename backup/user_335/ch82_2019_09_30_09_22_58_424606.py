def primeiras_ocorrencias(palavra):
    letrasExistentes = dict()
    for l in palavra:
        if not l in letrasExistentes:
            letrasExistentes[l] = 0
    i = 0
    for letra in letrasExistentes:
        if letra != palavra[i]:
            while letra != palavra[i]:
                i += 1
        else:
            letrasExistentes[letra] = i
            i += 1
    return letrasExistentes