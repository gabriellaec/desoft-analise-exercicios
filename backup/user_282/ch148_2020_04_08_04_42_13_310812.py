def conta_letras(palavra):
    lista = palavra
    count = dict()
    for letra in lista:
        if letra not in count:
            count[letra] = 1
        else:
            count[letra] += 1
    return count