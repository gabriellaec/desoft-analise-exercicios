distancia = float(input('Distância que deseja percorrer: '))
x=0
if distancia < 200:
    x = distancia * 0.5

else:
    x = (distancia - 200) * 0.45 + 100

print("Você vai pagar: R${0:.2f}".format(x) )