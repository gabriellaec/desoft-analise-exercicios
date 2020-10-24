a = float(input('Qual a velocidade do carro?'))

if(a>80):
    print('Você foi multado')
    print('Multa')
    print((5*(a-80)))

else:
    print('Não foi multado')