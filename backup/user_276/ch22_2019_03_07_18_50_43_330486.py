def eh_bissexto(ano):
    if ano % 400 == 0 and ano % 100 != 0:
        return "Ano bissexto"
    else:
        return "Não é bissexto"
    