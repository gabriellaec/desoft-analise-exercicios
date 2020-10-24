def eh_bissexto(ano):
    if ano%4==0 and ano%400:
        return True
    else:
        return False
       