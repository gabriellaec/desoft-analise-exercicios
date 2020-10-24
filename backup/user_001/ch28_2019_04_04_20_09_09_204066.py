velocidade = int(input("velocidade: "))
if velocidade > 80:
    multa = (velocidade-80)*5.00
    print("Você foi multado em R${0:.2f}".format(multa))
else:
    print("Não foi multado")