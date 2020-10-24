def eh_bissexto(ano):
    if ano % 100 == 0:
        if ano % 400 == 0:
            eh_bissexto=True
        else:
            eh_bissexto=False
    elif ano % 4 == 0:
        eh_bissexto = True
    else:
        eh_bissexto=False