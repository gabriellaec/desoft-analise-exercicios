km = int(input("Qual a velocidade seu carro está? "))
if km > 80:
 velocidade_extra = km-80
 multa = velocidade_extra*5
 print("Você está {0} km acima do limite de velocidade. Você foi multado em R${1}".format(velocidade_extra, multa))
else:
 print("Você está dentro do limite.")