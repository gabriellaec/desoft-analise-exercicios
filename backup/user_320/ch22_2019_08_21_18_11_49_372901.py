def eh_bissexto(ano):
    if int(ano) % 4 == 0:
       if int(ano) % 100 != 0:
           return True
    return False    