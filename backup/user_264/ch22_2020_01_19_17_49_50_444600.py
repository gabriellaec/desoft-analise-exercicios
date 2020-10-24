def eh_bissexto(ano):
    y = ano % 4
    x = ano % 100
    if y == 0 and x != 0:
        return True
    else:
        return False

