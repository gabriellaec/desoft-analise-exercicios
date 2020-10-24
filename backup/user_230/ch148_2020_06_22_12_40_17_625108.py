def conta_letras(string):
    lista=list(string)
    dicio={}
    for letra in lista:
        if letra in dicio:
            dicio[letra]+=1
        else:
            dicio[letra]=1
    return dicio