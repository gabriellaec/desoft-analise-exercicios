def eh_bissexto(ano):
    ano = int(input('Ano: '))
    if ano % 4 == 0:
        print('True')
    else:
        print('False')
    return ano
ano = eh_bissexto(ano)