ve=int(input('Qual a velocidade do carro? '))
    
if ve>80:
    print('Foi multado')
    valor=ve*5-400
    print('valor a ser pago= {0:.2f}'.format(valor))
else:
    print('Não foi multado')