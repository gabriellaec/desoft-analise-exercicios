def eh_bissexto(ano):
    if ano %4 == 0:
        return 'True'
    else:
        return 'False'

print(eh_bissexto(1950))