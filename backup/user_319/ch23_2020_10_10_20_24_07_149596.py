#qual a velocidade do carro?
# velocidade > 80Km/h , foi multado
# 
vel = input('qual a velocidade?')
if vel>80:
    return ("multado, a multa é {0:.2f}".format((vel-80)*5))
else:
    return não foi multado