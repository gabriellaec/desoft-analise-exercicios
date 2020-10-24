def velocidade(c):
    v=(c-80)*5
    return v
x = float(input('Qual a velocidade? '))
y=velocidade(x)
if y == 0:
    print('Não foi multado')
else:
    print ('Foi multado R$ '' {0:.2f}'.format (y))