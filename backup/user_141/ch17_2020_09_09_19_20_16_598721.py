def eh_bissexto(ano):
    if ano % 4 == 0 and ano != 100:
        bissexto = True
    else:
        bissexto = False 
    return bissexto