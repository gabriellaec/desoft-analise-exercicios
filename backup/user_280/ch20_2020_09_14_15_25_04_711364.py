distancia = int(input('Digite a distancia que quer percorrer: '))

if distancia <= 200:
    preço = 0.50*distancia
else:
    preço = 0.5*200 + 0.45*(distancia - 200)

print('{:.2f}'.format(preço))