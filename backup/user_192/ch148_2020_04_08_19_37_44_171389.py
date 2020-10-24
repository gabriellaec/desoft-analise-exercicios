def conta_letras(palavra):
    ocorrencias = {}
    for letras in palavra:
        if not letras in ocorrencias:
            ocorrencias[letras] = 1
        else:
            ocorrencias[letras] += 1
    return ocorrencias