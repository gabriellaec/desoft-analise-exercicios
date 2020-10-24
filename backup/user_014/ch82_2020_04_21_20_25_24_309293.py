def primeiras_ocorrencias(string):
    s = str(string)
    contagem = {}
    i = 0
    while i < len(s):
        if not caractere in contagem:
            contagem[caractere] = 1
        else:
            contagem[caractere] += 1
    return contagem