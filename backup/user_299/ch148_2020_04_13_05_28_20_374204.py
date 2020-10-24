def conta_letras(string):
    letras = []
    for i,e in enumerate(string):
        e = string[i:i+1]
        letras.append(e)
    contdel = {}
    for g in letras:
        if g in contdel:
            contdel[g] = contdel[g] + 1
        else:
            contdel[g] = 1
    return contdel