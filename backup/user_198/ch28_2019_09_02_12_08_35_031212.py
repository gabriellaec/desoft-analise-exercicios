velo=float(input("Entre com a velocidade, em km/h: "))
if velo>80:
    multa=5*(velo-80)
    print("Você foi multado em {0:.2f} reais, pois ultrapassou o limite de 80km/h".format(multa))  
else: print("Não foi multado") 