def eh_bissexto(ano):
    y = ano % 400
    if y == 0:
        return True
    else:
        return False

