def eh_bissexto(ano):
    if a%400:
        return True
    elif a%400 and a%100:
        return False
    elif a%4:
        return True
    else:
        return False