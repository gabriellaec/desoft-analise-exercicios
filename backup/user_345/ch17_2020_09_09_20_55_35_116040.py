def eh_bissexto(ano):
    if ano % 4 == 0:
        return 'True'
    else:
        return 'False'

a = int(input('qual year: '))
print (eh_bissexto(a))