v = float(input('Qual a velocidade do carro?'))
if v < 0:
    print ('inválido')
elif v <= 80:
    print ('Não foi multado')
else:
    valor = 0.5*(v - 80)
    print ('Foi multado no valor de {0:.2f}'.format(valor))

