def eh_bissexto(ano):
    if ano % 4 == 0:
        return "True"
    elif ano == 1:
        return "True"
    else:
        return "False"