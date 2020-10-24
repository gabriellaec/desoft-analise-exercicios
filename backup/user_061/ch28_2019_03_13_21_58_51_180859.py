velocidade = float(input("Velocidade atual"))

if velocidade > 80:
    print("Você foi multado")
    multa = (velocidade - 80)*5
    print('{0:.2f}'.format(multa))
else:
    print("Não foi multado")