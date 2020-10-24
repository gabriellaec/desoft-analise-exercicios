def conta_letra(texto):
    contagem={}
    for letra in texto:
        if not letra in texto:
            contagem[letra]=1
        else:
            contagem[letra]+=1
    return contagem