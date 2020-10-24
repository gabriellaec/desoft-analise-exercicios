def eh_bissexto(ano):
    if ano % 4 == 0:
        print('True')
    else:
        print('False')
    return ano
ano = int(input('Ano: '))
eh_bissexto(ano)
