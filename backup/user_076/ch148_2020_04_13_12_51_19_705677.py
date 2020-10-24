def conta_letras (string):
    letra_frequencia = dict()
    for i in string:
        if i not in letra_frequencia:
            letra_frequencia[i] = 1
        else:
            letra_frequencia[i] +=1
    return letra_frequencia