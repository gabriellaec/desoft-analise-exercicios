def eh_bissexto(ano):
    y = ano %4
    x = ano %100
    z = ano %400
    if y == 0:
        return True
    elif x == 0:
        if z == 0:
            return True
    else:
        return False
