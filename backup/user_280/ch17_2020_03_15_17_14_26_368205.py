def eh_bissexto(ano):
    y = ano % 4
    return y

if eh_bissexto == 0:
    return True
else:
    return False