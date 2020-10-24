def eh_crescente(lista):
    previous = lista[0]
    for number in lista:
        if number < previous:
            return False
        previous = number
    return True