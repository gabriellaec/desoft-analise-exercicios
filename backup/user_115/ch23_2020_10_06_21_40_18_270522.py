v = int(input("Qual a velocidade do carro?"))
if v > 80:
    multa = 5*(v-80)
    print("Você foi multado, custando: R${:.2f}".format(multa))
else:
    print("Não foi multado")