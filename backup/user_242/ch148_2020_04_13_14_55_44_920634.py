def conta_letras(string):
    dicionario ={}
    for letra in string:
            dicionario[letra] = string.count(letra)
    return dicionario
            