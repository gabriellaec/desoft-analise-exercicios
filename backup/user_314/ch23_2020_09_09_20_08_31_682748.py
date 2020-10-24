velocidade= float(input("Velocidade (km/h):"))

if(velocidade>80):
    multa=5*(velocidade-80)
    print("Você foi multado: {:.2f}".format(multa))
else:
    print("Não foi multado")