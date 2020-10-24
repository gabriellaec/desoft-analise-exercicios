def eh_bissexto(ANO):
    if ANO % 4 == 0 and ANO % 100 != 0 or ANO % 400 == 0 and ANO != 1:
        return True
    else:
        return False