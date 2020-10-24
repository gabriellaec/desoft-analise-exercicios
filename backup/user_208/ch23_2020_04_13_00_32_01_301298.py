velocidade = int(input("Qual a velocidade do carro? "))
if velocidade > 80:
    multa = (velocidade-80)*5
    print ("Você foi multado em R$ {0:.2f}".format(multa))
else:
    print ("Você não foi multado")
    
