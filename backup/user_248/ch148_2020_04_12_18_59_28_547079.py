def conta_letras(texto):
    contagem=dict()
    for letra in texto:
        if not letra in texto:
            contagem[letra] = 1
        else:
            contagem[letra] += 1
    return contagem