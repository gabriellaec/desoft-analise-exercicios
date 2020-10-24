def apaga_repetidos(texto):
    saida = ''
    for i in range(len(texto)):
        letra = texto[i]
        for j in range(len(saida)):
            caractere = saida[j]
            if letra not in caractere:
                saida = saida + letra
            else:
                letra == '*'
                saida = saida + letra
    return saida
    