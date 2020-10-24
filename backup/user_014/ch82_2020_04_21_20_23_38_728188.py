def primeiras_ocorrencias(string):
    s = str(string)
    contagem = {}
    for caractere in s:
        if not caractere in contagem:
            contagem[caractere] = 1
        else:
            contagem[caractere] += 1
    return contagem