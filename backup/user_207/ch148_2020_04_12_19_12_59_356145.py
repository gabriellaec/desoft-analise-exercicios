def conta_letras (string):
    dicio = {}
    for letra in string:
        if letra in dicio:
            dicio[letra] +=1
        else:
            dicio[letra] =1
    return dicio