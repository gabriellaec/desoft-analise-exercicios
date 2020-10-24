def eh_bissexto(ANO):
    if ANO % 4 == 0 and ANO % 100 != 0 or ANO % 400 == 0:
        return 'É bissexto'
    elif ANO == 1:
        return 'Não é bissexto'
    else:
        return 'Não é bissexto'