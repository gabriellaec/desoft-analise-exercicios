def eh_bissexto(ano):
    y = ano % 4
    return y

if eh_bissexto == 0:
    eh_bissexto = True
else:
    eh_bissexto = False