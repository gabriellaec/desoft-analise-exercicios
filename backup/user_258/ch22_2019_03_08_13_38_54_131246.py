def eh_bissexto (ano):
    if ano%100==0:
        return 'False'
    else ano%400==0 and ano%4==0:
        return 'True'
    