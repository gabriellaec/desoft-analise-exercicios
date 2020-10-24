def conta_letras(texto):
    dicionario={}
    for letra in texto:
        if not letra in dicionario:
            dicionario[letra]= 1
        else:
            dicionario[letra]+= 1
    return dicionario