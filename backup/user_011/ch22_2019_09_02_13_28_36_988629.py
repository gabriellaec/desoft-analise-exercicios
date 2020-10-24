def eh_bissexto(ano):    
    bissexto = True
    if ano%4 == 0:
        return bissexto
    elif ano%100 == 0:
        bissexto = False
    elif ano%400 == 0:
        return bissexto