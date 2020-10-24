def eh_bissexto(ano):

    if ano%400 == 0:
        return True
    if ano%100 == 0:
        return False
    if ano%4 == 0:
        return True
    return False