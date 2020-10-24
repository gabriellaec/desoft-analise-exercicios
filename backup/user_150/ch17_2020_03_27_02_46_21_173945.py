def eh_bissexto(ano):
    bissexto = 4
    if ano % bissexto == 0:
        return 'True'
    else:
        return 'False'