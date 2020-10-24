velocidade = int(input('velocidade: '))
if velocidade>80:
	preco_multa=(velocidade-80)*5
    print("{:.2f}".format(preco_multa))
else:
    print('Não foi multado')


    