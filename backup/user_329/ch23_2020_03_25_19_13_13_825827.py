v = int(input("Qual a velocidade do seu carro?"))

if v>80:
    multa = (v-80)*5
    print("Você foi multado, o valor da multa é de {0}".format(multa))
else:
    print("Você não foi multado.")