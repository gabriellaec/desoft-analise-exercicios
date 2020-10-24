velocidade = int(input("Qual a velocidade do seu carro?"))
if velocidade > 80:
     multa = (velocidade-80)*5
    print("Você foi multado por R${0:.2f}" .format(multa))
elif velocidade <= 80:
    print("Não foi multado.")