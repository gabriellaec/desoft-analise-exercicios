def eh_bissexto(ano):
    if ano%4==0:
        return 'é bi'
    elif not ano%4==0:
        return 'não é bi'