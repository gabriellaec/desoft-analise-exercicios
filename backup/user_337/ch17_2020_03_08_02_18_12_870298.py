def eh_bissexto (ano):
    if ano%400 == 0:
        return 'bissexto'
    else:
        return 'não bissexto'