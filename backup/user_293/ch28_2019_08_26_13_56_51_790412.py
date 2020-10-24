km = int(input("Qual a velocidade do seu carro?: "))

if km > 80:
    multa = (km - 80)*5
    print("Voce foi multado:R${0:.2f}".format(multa))
else:
    print("Não foi multado")
