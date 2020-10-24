def eh_bissexto(ano):
    ano = int(input())
    bissexto = ano%4
    if bissexto != 0:
        return False
    else:
        return True