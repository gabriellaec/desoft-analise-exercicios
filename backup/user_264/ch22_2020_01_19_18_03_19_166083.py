def eh_bissexto(ano):
    y = ano %4
    x = ano %100
    if y == 0:
        return True
    elif x != 0:
        return False