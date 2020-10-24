def conta_letras(string):
    dicionario={}
    for caractere in string:
        if not caractere in dicionario:
            dicionario[caractere]=string.count(caractere)
    return dicionario