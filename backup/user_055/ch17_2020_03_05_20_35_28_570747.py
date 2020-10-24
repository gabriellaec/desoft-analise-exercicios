def eh_bissexto(ano):
    ano = int(input('O ano é: '))
    if ano % 4 == 0:
        return True
    else:
        return False
    return ano