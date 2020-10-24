a = int(input("Velocidade do carro de um usuário"))
if a <=80:
    print("Não foi multado")
else:
    multa = (a - 80)*5
    print("Voce foi multado: R${0}".format(multa))