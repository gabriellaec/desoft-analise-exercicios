def eh_bissexto(ano):    
    bissexto = True
    if ano%400 == 0:
        return bissexto
    elif ano%100 == 0:
        return False
    elif ano%4 == 0:
        return bissexto
    else:
        return False