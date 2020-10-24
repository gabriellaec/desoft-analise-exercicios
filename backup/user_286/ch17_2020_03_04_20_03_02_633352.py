def eh_bissexto (ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        x = True
    else:
        x = False

    return x