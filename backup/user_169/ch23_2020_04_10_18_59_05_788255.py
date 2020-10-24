velocidade=int(input("Qual é a velocidade do carro?"))

multa=(velocidade - 80)*5

if velocidade>80:
    print('você foi multado e esse é o valor da sua multa R$ %.2f' % (multa))

else:
    print('Não foi multado')