velocidade= float(input("Velocidade (km/h): \n"))

if(velocidade>80):
    multa=5*(velocidade-80)
    print("Você foi multado: {:.2f}")
else:
    print("Não foi multado")