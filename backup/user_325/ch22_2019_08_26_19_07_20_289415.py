def eh_bissexto(ano):
    if ((ano%4 == 0) and (ano != 1) and not(ano%100)):
        return True
    else:
        return False
