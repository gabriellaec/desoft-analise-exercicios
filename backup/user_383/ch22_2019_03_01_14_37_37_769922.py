def eh_bissexto(ano):
    if ano % 400 == 0 and ano % 100 != 0:
        return('True')
    elif ano % 100 == 0 and ano % 400 != 0:
        return('False')
    else:
        return('True')
ano=int(input('Qual é o ano o qual você deseja consultar se ele é bissexto? :'))
print(eh_bissexto(ano))
