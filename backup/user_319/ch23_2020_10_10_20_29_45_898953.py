#qual a velocidade do carro?
# velocidade > 80Km/h , foi multado
vel = int(input('qual a velocidade?'))
if vel>80:
    print("multado, a multa é {0:.2f}".format((vel-80)*5))
else:
    print("não foi multado")