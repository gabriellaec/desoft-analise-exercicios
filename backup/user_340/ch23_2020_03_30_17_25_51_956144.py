a=float(input('qual a velocidade do carro?'))
if a>80:
    b=int('R$5*(a-80)')
    print('foi multado em R${0}'.format(b))
else:
          print('Não foi multado')