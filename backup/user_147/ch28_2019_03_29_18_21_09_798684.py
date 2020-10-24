v = float(input())

if v > 80:
    print('bla')
    print('{0:.2f}'.format((v - 80)*5))
else:
    print('Não foi multado')