def eh_bissexto(ano):
    if ano%4 == 0 and not(ano%100) or ano%400:
        return True
    else:
        return False
