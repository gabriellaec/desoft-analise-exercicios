def eh_bissexto(ano):
    a = ano
    if a % 4 == 0 or a % 400 == 0 and not a % 100 == 0:
        return True
    else:
        return 'false'

c= eh_bissexto(1)
print(c)