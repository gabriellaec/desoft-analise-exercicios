def eh_bissexto(ano):
    if ano%4==0:
        return 'é bissexto'
    elif not ano%4==0:
        return 'não é bissexto'