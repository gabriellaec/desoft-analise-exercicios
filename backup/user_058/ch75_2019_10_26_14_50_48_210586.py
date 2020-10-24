def verifica_primos(lista):
    dicionario = {}
    for i in lista:
        if i == 1:
            dicionario[i] = False
        elif i == 2:
            dicionario[i] = True
        elif i == 3 or i == 5 or i == 7 or i == 11 or i == 13:
            dicionario[i] = True
        elif i%2 == 0 or i%3 == 0:
            dicionario[i] = False
        elif i%5 == 0 or i%7 == 0:
            dicionario[i] = False
        elif i%11 == 0 or i%13 == 0:
            dicionario[i] = False
        else:
            dicionario[i] = True
    return dicionario