def eh_bissexto(ano):
    y = ano % 4
    x = ano % 10
    if y == 0 or x == 0:
        return True
    else:
        return False
    return y

