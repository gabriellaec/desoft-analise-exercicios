def eh_bissexto (ano):
    if ano % 4 == 0 and ano >= 1000 and  ano % 400 == 0 or ano % 100 != 0:
        return True
    else:
        return False