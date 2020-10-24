a=int(input('Qual é a velocidade do seu carro?'))
if a > 80:
    print ('Você foi multado. Deve pagar R$:{0:.2f}'.format((a-80)*5))