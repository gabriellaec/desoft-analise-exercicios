def conta_bigramas(x):
    dic_notas = {}
    i = 0
    for e in x:
        palavra = e[0] + e[1]
        dic_notas[palavra] = i
        i+=1
    return palavra 