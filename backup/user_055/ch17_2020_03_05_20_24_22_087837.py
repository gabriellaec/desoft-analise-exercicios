def eh_bissexto(ano):
    if ano % 4 == 0:
        return True
    else:
        return False
    return ano

ano = int(input('Qual é o ano: '))
eh_bissexto(ano)