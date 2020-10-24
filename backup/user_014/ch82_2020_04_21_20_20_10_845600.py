def primeiras_ocorrencias(string):
    contagem = {}
    for caractere in string:
        if not caractere in contagem:
            contagem[caractere] = 1
        else:
            contagem[caractere] += 1
    return contagem