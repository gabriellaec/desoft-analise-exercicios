def conta_letras (texto):
    contagem = {}
    for letras in texto:
        if not letras in contagem:
            contagem[letras] = 1
        else:
            contagem[letras] += 1
    return contagem