def eh_bissexto(ano):
    if ano%4!=0:
        return False
    elif ano%100==0 and %4==0:
        return False
    elif ano%100==0 and ano%400!=0:
        return False
    else:
        return True
    