def eh_bissexto(ano):
    if int(ano/400)/(ano/400)==1:
        return "bissexto"
    elif int(ano/100)/(ano/100) == 1:
        return "não bissexto"
    elif int(ano/4)/(ano/4) == 1:
        return "bissexto"
    else:
        return "nao bissexto"