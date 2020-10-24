def eh_bissexto (ano):
    if ano%400==0:
        return str('True')
    if ano%100==0:
        return str('False')
    elif ano%4==0:
        return str('True')
    else:
        return str('False')
    
    