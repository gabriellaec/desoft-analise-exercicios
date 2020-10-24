distancia = float(input('Distância que deseja percorrer: '))

if distancia < 200:
    preco = 0.5

else:
    preco = 0.45

print("Você vai pagar este mês: R$%6.2f" % (distancia * preco))