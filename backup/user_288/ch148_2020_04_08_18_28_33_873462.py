def conta_letras (texto):
    contagem = {}
    for letra in texto:
        if not letra in contagem:
            contagem[letra] =1
        else:
            contagem[letra] += 1
    return contagem