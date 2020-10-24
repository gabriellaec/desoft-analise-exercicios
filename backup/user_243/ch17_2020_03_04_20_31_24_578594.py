def eh_bissexto(ano):
    if ano%100!=0 and ano%4==0:
        return "true"
    elif ano%400==0:
        return "true"
    else:
        return "false"
