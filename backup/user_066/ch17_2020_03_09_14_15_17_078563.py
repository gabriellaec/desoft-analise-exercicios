def eh_bissexto(ano):
    b= ano
    if (ano%4 == 0 and ano%100 != 0) or ano%400 == 0 or ano == 1:
        a = True
    else:
        a = False
    return a