def eh_bissexto (ano):
    if ano%100 == 0:
        if ano%400 == 0:
            return 'True'
        else:
            return 'False'
    else:
        if ano%4 == 0:
            return 'True'
        else:
            return 'False'