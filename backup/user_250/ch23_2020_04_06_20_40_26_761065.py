v = float(input("Qual a velocidade do carro? "))
if v > 80:
    q = v-80
    multa = format(q*5, '.2f')
    print("Multa = {0}".format(multa))
else:
    print("Não foi multado")
    