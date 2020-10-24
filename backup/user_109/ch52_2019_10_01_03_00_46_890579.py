def eh_crescente(lista):
    maior = lista[0]
    i = 1
    contador = 0

    while i < len(lista):
        if lista[i] > maior:
            lista[i] = maior
            contador += 1
        i += 1

    if contador == (len(lista) - 1):
        return True
    else:
        return False