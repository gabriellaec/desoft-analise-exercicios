def conta_letras(string):
    dicionario = {}
    for letra in string:
        i = dicionario.get(letra,0)
        i += 1
        dicionario[letra] = i
    return dicionario
        