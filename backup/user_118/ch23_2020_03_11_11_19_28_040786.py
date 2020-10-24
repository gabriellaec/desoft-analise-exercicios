def velocidade(c):
    v=(c-80)*5
    return v
x = input('Qual a velocidade? ')
y=velocidade(x)
if y == 0:
    print('Não foi multado')
else:
    print ('Valor da multa R$ '' {0:.2f}'.format (y))