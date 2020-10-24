def conta_ocorrencias (texto):
    contagem = {}
    for palavra in texto:
        if not palavra in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    return contagem