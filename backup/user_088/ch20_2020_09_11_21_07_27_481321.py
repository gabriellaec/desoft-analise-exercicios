distancia=float(input('digite a distancia'))
if (distancia<=200):
preco=0,5*(distancia)
print ('o preco é R${0:.2f}'.format(preco))
else:
preco=(distancia)*0,45
print('o preco é R${0:.2f}'.format(preco))