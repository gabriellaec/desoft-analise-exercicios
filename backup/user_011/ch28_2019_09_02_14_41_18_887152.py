vel = int(input("Qual a vel? "))
if vel > 80:
    multa = (vel - 80)*5
    print("Multado, R$ {0}".format(multa))
else:
    print("Não foi multado")