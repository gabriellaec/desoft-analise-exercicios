def primeiras_ocorrencias(string):
    dicionario_indices = {}
    contador = 0
    for letra in string:
        if letra not in dicionario_indices:
            dicionario_indices[letra] = contador
        contador += 1
    return dicionario_indices