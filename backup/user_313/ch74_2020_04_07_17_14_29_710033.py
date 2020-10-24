def conta_bigramas(a):
    dicionario = {}
    for i in range(0,len(a),1):
        novo = a[i]+a[i-1]
        if novo not in dicionario:
            dicionario[novo] = 1

        else:
            dicionario[novo] += 1

    return(dicionario)