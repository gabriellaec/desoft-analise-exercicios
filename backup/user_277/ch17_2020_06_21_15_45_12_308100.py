def eh_bissexto(ano):
    if ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False
        