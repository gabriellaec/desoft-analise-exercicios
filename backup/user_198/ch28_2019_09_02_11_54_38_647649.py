velo=int(input("Entre com a velocidade, em km/h: "))
if velo>80:
    multa=5*(velo-80)
    print("Você foi multado em {0} reais, pois ultrapassou o limite de 80km/h".format(multa))           