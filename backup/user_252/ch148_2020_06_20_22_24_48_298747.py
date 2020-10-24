def conta_letras(texto):
    dicio={}
    for letra in texto:
        if not letra in dicio:
            dicio[letra]=1
        else:
            dicio[letra]+=1
    return dicio
            