def eh_crescente(lista):
     previous = list[0]
    for number in list:
        if number < previous:
            return False
        previous = number
    return True