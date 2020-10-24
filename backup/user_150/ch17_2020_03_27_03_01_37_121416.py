bissexto = 4
cem = 100
quatrocentos = 400
def eh_bissexto(ano):
    if ano % cem == 0 and ano % quatrocentos != 0:
    if ano % bissexto == 0:
        return 'True'
    else:
        return 'False'