def conta_letras(string):
    dicionario = {}
    lista_letras = list(string)
    for letra in lista_letras:
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1
    return dicionario   