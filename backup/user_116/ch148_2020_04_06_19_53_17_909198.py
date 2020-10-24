def conta_letras(string):
    dicionario={}
    for e in string:
        dicionario[e]=string.count(e)
    return dicionario 