def eh_bissexto(ano):
    if ano%4 == 0 and ano%100 != 0:
        return TRUE
    elif ano%4 != 0 and ano%400 == 0:
        return TRUE
    else:
        return FALSE