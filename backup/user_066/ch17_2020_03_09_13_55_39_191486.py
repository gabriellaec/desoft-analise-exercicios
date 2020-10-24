def eh_bissexto(ano):
    if (ano%4 == 0 and not ano%100 == 0) or ano%400 == 0 or ano == 1:
        a = True
    else:
        a = False
    return a