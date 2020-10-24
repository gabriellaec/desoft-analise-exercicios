def conta_letras(string):
    dicionario ={}
    for i in string:
            dicionario[string[i]] = string.count(i)
    return dicionario
            