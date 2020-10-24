def eh_bissexto(ANO):
    if ANO % 4 == 0 and ANO % 100 != 0 or ANO % 400 == 0:
        return 'É bissexto'
    else:
        return 'Não é bissexto'