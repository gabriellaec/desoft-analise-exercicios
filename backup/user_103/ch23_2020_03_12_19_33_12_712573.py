a=int(input('Qual é a velocidade do seu carro?'))
if a > 80:
    print ('Você foi multado.')
if a > 80:
    print ('Deve pagar R$:{0:.2f}'.format((a-80)*5))
else:
    print('Não foi multado')
