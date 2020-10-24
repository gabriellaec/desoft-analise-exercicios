def primeiras_ocorrencias(string):
    contagem = {}
    i = 0
    for caracteres in string:
        if not caracteres in contagem:
            contagem[caracteres] = i
        i += 1
    return contagem