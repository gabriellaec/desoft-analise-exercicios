vel = int(input("Qual a velocidade do seu carro?"))
if vel>80:
    print ("Você ultrapassou o limite e levará uma multa")
    multa = (vel-80)*5
    print ("{:12.2f}".format(multa))