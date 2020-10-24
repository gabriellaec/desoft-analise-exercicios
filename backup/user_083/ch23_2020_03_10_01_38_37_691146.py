a= int(input('Qual sua velocidade: '))
if a > 80:
    b=(a-80)*5
    print('A multa sera de: R$ {0:.2f}'.format(b))
else:
    print('Não foi multado')