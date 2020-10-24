def conta_letras(texto):
    D = {}
    for letra in texto:
        if letra in D:
            D[letra]+=1
        else:
            D[letra]=1
            
    return D     