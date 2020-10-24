velocidade = float(input("Qual a velocidade do carro?"))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você foi multado")
    print("{0:.02f}".format(multa))
else:
	print("Não foi multado")
          
          