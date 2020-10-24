def eh_bissexto (ano):
    if ano == 1:
        return 'True'
    elif ano % 4 == 0 or ano % 100 != 0 :
        return 'True'
    else:
        return 'False'

