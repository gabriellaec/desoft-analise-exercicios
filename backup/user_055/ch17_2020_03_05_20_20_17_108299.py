def eh_bissexto(ano):
    ano = int(input('Qual é o ano: '))
    if ano%4 == 0:
        return True
    else:
        return False
    return ano