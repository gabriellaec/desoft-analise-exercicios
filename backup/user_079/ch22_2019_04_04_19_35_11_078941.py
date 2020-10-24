def eh_bissexto(ano):
    x= ano
    if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
        return True
    else False