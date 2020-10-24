def eh_bissexto(ano):
    if ano % 400 == 0:
        status_bissexto = True
    elif ano % 100 == 0:
        status_bissexto = False
    elif ano % 4 == 0:
        status_bissexto = True
    else:
        status_bissexto = False
    return status_bissexto