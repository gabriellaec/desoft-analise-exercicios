a = float(input('Qual a velocidade do seu carro ? '))

if ( a > 80):
    print('Você foi multado em R$:' )
    print('%.2f' % ((a-80)*5))

else:
    print('Não foi multado')