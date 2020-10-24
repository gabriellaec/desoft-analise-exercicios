vel_carro = int(input('Qual a velocidade do carro? '))

if vel_carro > 80:
    km_multa = 80 - vel_carro
    preco_multa = km_multa * 5
    print ('Você foi multado pelo valor de {0:.2f}, otário'.format(preco_multa))

else:
    print ('Não foi multado')
     