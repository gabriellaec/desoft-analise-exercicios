def eh_bissexto(ano):
    if ano%100!=0:
        return "true"
    elif ano%4==0:
        return "true"
    else:
        return "false"
