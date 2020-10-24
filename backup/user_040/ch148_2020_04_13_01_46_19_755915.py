dicionario = {}
def conta_letras(x):
    for letra in x:
        if letra not in dicionario:
            dicionario[letra] = 1
        else:
            dicionario[letra] += 1
return dicionario