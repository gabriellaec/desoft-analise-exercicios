def conta_letras(string):
    dicionario = {}
    for i in range(len(string)):
        letra = string[i]
        if letra not in dicionario.keys():
            dicionario[letra] = 1
        else:
            deicionario[letra] +=1
    return dicionario
        