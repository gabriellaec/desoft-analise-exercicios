multa=0
velocidade=int(input("Qual a velocidade do carro? "))
if velocidade>80:
    multa=5*(velocidade-80)
    print("A multa foi de R${0:.2f}".format(multa))
else: 
    print("Não foi multado")