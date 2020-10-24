v = (input("Qual a velocidade do seu carro?"))

if v>80:
    multa = (v-80)*5.00
    print("Você foi multado, o valor da multa é de R${0}".format(multa))
else:
    print("Não foi multado.")